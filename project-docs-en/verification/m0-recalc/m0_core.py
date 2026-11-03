"""
Independent M0 recalculation core (Python standard library only).

Implements the M0 definitions from project-docs/analysis/KINSHIP-MATHEMATICAL-REFERENCE.md
(sections B and C). Written from the definitions, not from the author's architecture.

  B.1(5)  the ancestor graph must be acyclic
  C.1     upward path (identity path has length 0)
  C.3     number of paths (distinct upward sequences)
  C.4     COMMON(A,B)
  C.5     valid path pair: vertex sets intersect exactly in the common ancestor
  C.6     J = ancestors with at least one valid pair
  C.7     R = number of valid pairs over all of J
  C.8-9   a, b, L = a + b
  C.10    direct line when min(a,b) = 0; generation distance max(a,b)
  C.11    sibling (1,1)
  C.12    avuncular (1,2) or (2,1)
  C.13    cousin degree min(a,b) - 1 and removal |a - b|, only when a,b >= 2
"""

ROLES = ("FATHER", "MOTHER")


class GraphError(Exception):
    """Raised when a graph violates the M0 graph rules (B.1)."""


def build_graph(people):
    graph = {}
    for person in people:
        pid = person["id"]
        if pid in graph:
            raise GraphError(f"duplicate person id {pid}")
        graph[pid] = {"FATHER": person.get("father_id"), "MOTHER": person.get("mother_id")}
    for pid, parents in graph.items():
        for role in ROLES:
            parent = parents[role]
            if parent is not None and parent not in graph:
                raise GraphError(f"{pid} references unknown {role} {parent}")
    assert_acyclic(graph)
    return graph


def assert_acyclic(graph):
    """B.1(5): depth-first search with white/grey/black colouring; a grey hit is a cycle."""
    white, grey, black = 0, 1, 2
    colour = {pid: white for pid in graph}

    def visit(node):
        colour[node] = grey
        for role in ROLES:
            parent = graph[node][role]
            if parent is None:
                continue
            if colour[parent] == grey:
                raise GraphError(f"biological cycle: {node} -> {parent}")
            if colour[parent] == white:
                visit(parent)
        colour[node] = black

    for pid in graph:
        if colour[pid] == white:
            visit(pid)


def upward_paths(graph, start):
    """Map ancestor -> list of (nodes, roles) for every upward path from start (C.1)."""
    found = {}

    def walk(nodes, roles):
        found.setdefault(nodes[-1], []).append((tuple(nodes), tuple(roles)))
        for role in ROLES:
            parent = graph[nodes[-1]][role]
            if parent is not None:
                walk(nodes + [parent], roles + [role])

    walk([start], [])
    return found


def compute(graph, a_id, b_id):
    """Return COMMON, J, valid pairs (C.5), and the count of rejected candidate pairs per ancestor."""
    paths_a = upward_paths(graph, a_id)
    paths_b = upward_paths(graph, b_id)
    common = sorted(set(paths_a) & set(paths_b))
    valid = []
    invalid_count = {}
    for ancestor in common:
        for pa in paths_a[ancestor]:
            for pb in paths_b[ancestor]:
                if set(pa[0]) & set(pb[0]) == {ancestor}:
                    valid.append((ancestor, pa, pb))
                else:
                    invalid_count[ancestor] = invalid_count.get(ancestor, 0) + 1
    junctions = sorted({anc for anc, _, _ in valid})
    return {
        "common": common,
        "junctions": junctions,
        "valid": valid,
        "invalid_count": invalid_count,
        "paths_a": paths_a,
        "paths_b": paths_b,
    }


def pair_record(ancestor, pa, pb):
    a = len(pa[0]) - 1
    b = len(pb[0]) - 1
    return {
        "ancestor_id": ancestor,
        "path_a": {"nodes": list(pa[0]), "roles": list(pa[1]), "length": a},
        "path_b": {"nodes": list(pb[0]), "roles": list(pb[1]), "length": b},
        "a": a,
        "b": b,
        "L": a + b,
    }


def canonical(rec):
    """Identity key for a valid pair: ancestor plus both node and role sequences."""
    return (
        rec["ancestor_id"],
        tuple(rec["path_a"]["nodes"]),
        tuple(rec["path_a"]["roles"]),
        tuple(rec["path_b"]["nodes"]),
        tuple(rec["path_b"]["roles"]),
    )


def classify(a, b):
    """Conservative structural class (M0 C.10-C.13 and section D)."""
    if min(a, b) == 0:
        return "direct_line"
    if (a, b) == (1, 1):
        return "sibling"
    if sorted((a, b)) == [1, 2]:
        return "avuncular"
    if a >= 2 and b >= 2:
        return "cousin"
    return "other"


def max_paths_per_ancestor(graph, a_id, b_id):
    """Largest number of upward paths to one ancestor on either side (C.3)."""
    res = compute(graph, a_id, b_id)
    best = 1
    for side in (res["paths_a"], res["paths_b"]):
        for paths in side.values():
            best = max(best, len(paths))
    return best
