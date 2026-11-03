import 'package:flutter/material.dart';

/// Entry point for the sovereign lineage app (skeleton, P0).
void main() {
  runApp(const SovereignLineageApp());
}

class SovereignLineageApp extends StatelessWidget {
  const SovereignLineageApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Sovereign Lineage',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.teal),
      ),
      home: const HomeScreen(),
    );
  }
}

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Sovereign Lineage'),
      ),
      body: const Center(
        child: Text('Family tree and kinship discovery'),
      ),
    );
  }
}