This repo contains `solution.py`, which adds a calculated (virtual) column to a pandas DataFrame using a simple expression over existing columns.

- Allowed operators: `+`, `-`, `*`
- Column labels: letters and underscores only
- Invalid input returns an empty DataFrame

Additionally, I have created 3 extra tests: `test_invalid_operator_exponent`, `test_cannot_overwrite_existing_column`, `test_empty_when_non_numeric_types`.

## Run tests

- Sample tests (provided by client):
  - `pytest -q test_virtual_column.py`
- Additional tests added (3 extra):
  - `pytest -q test_additional.py`
- Run all:
  - `pytest -q`
