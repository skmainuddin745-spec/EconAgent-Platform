# Contributing to EconAgent Platform

Thank you for your interest in contributing to the **EconAgent Platform**. We welcome contributions from quantitative analysts, economists, software engineers, and domain researchers.

## Development Principles
1. **Zero-Hallucination Integrity:** Every proposed calculation or metric must trace directly to empirical source files (Damodaran datasets, exchange filings, or validated public APIs). No statistical figures may be synthesized or approximated without code-backed provenance.
2. **Evidence Citations:** Any new agent must attach `EvidenceCitation` records carrying the source file path, byte checksum (SHA-256), column target, sample size, and plain-language interpretation.
3. **Econometric Bounds:** Every metric must pass the harness sanity guardrails (`SANITY_BOUNDS`) defined in `run_platform.py`.
4. **Deterministic Reproducibility:** The full 6-stage pipeline (`py -3.12 run_platform.py`) must execute cleanly and achieve $\ge 98.0\%$ verification.

## Submitting Pull Requests
1. Fork the repository and create a feature branch (`git checkout -b feature/agent-enhancement`).
2. Implement your changes adhering to PEP 8 standards for Python and modular ES6 for browser components.
3. Execute `py -3.12 run_platform.py` to confirm that all 18 agents produce validated results and that `EconAgent_Dashboard.html` compiles without errors.
4. Commit your changes with descriptive Conventional Commit messages (`feat: ...`, `fix: ...`, `docs: ...`).
5. Open a Pull Request referencing relevant methodology papers or empirical data sources.

