import pandas as pd
from solution import add_virtual_column


def test_invalid_operator_exponent():
    df = pd.DataFrame([[2, 3]] * 2, columns = ["label_one", "label_two"])
    df_result = add_virtual_column(df, "label_one ** label_two", "label_three")
    assert df_result.empty, f"Should return an empty df when an unsupported operator is used: '**'.\n\nResult:\n\n{df_result}\n\nExpected:\n\nEmpty df"


def test_cannot_overwrite_existing_column():
    df = pd.DataFrame([[1, 1, 0]] * 2, columns = ["label_one", "label_two", "label_three"])
    df_result = add_virtual_column(df, "label_one + label_two", "label_three")
    assert df_result.empty, f"Should return an empty df when trying to overwrite an existing column: 'label_three'.\n\nResult:\n\n{df_result}\n\nExpected:\n\nEmpty df"


def test_empty_when_non_numeric_types():
    df = pd.DataFrame([[1, "x"]] * 2, columns = ["label_one", "label_two"])
    df_result = add_virtual_column(df, "label_one + label_two", "label_three")
    assert df_result.empty, f"Should return an empty df when referenced columns are non-numeric.\n\nResult:\n\n{df_result}\n\nExpected:\n\nEmpty df"
