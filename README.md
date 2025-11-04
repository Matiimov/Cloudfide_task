This repo contains `solution.py`, which adds a calculated (virtual) column to a pandas DataFrame using a simple expression over existing columns.

- Allowed operators: `+`, `-`, `*`
- Column labels: letters and underscores only
- Invalid input returns an empty DataFrame

## Run tests

- Sample tests (provided by client):
  - `pytest -q test_virtual_column.py`
- Additional tests added (3 extra):
  - `pytest -q test_additional.py`
- Run all:
  - `pytest -q`
