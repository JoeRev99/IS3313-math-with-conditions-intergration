name: CI

on:
  push:
  pull_request:

jobs:
  run_tests:
    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        python-version:
          - "3.9"
          - "3.10"
          - "3.11"
          - "3.12"
    name: Test
    runs-on: ${{ matrix.os }}

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install dependencies
        run: python -m pip install pytest

      - name: Run tests
        run: pytest
