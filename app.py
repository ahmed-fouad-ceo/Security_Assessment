name: Bandit Security Scan

on:
  push:
    branches:
      - main

jobs:
  bandit_scan:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v2

      - name: Set Up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.9

      - name: Install Dependencies
        run: pip install bandit

      - name: Run Bandit Security Scan
        run: bandit -r .
