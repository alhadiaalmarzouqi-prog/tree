import 'package:flutter_test/flutter_test.dart';

import 'package:sovereign_lineage_app/main.dart';

void main() {
  testWidgets('shows the sovereign lineage home screen', (WidgetTester tester) async {
    await tester.pumpWidget(const SovereignLineageApp());

    expect(find.text('Sovereign Lineage'), findsWidgets);
    expect(find.text('Family tree and kinship discovery'), findsOneWidget);
  });
}