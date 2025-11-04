import pandas as pd
import re
from pandas.api.types import is_numeric_dtype


def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    """
    Add a virtual column to a DataFrame based on a mathematical expression.
    
    Constraints:
        - Only column-to-column operations are supported.
        - Allowed operators: +, -, * (single char only).
        - Column labels must contain only letters and underscores.
        - The new column must not already exist in the DataFrame.
    
    Args:
        df: Source pandas DataFrame
        role: Mathematical expression defining the calculation (e.g., "col_a + col_b")
        new_column: Name for the new virtual column
        
    Returns:
        pandas.DataFrame: New DataFrame with the virtual column added, or empty DataFrame if validation fails
    """
    
    # Validate input type
    if not isinstance(df, pd.DataFrame):
        return pd.DataFrame()

    # Validate new column name: must contain only letters and underscores
    if not isinstance(new_column, str) or not _is_valid_column_name(new_column):
        return pd.DataFrame()
    
    # Forbid overwriting an existing column
    if new_column in df.columns:
        return pd.DataFrame()
    
    # Clean the role expression by stripping leading/trailing spaces
    if not isinstance(role, str):
        return pd.DataFrame()
    role_cleaned = role.strip()
    if not role_cleaned:
        return pd.DataFrame()
    
    # Validate the expression grammar early
    if not _is_valid_expression(role_cleaned):
        return pd.DataFrame()

    # Extract all potential column names from the role expression
    column_references = _extract_column_names(role_cleaned)
    
    # Validate all extracted column names
    for col_name in column_references:
        if not _is_valid_column_name(col_name):
            return pd.DataFrame()
    
    # Check if all referenced columns exist in the DataFrame
    for col_name in column_references:
        if col_name not in df.columns:
            return pd.DataFrame()
    
    # Ensure all referenced columns are numeric
    for col_name in column_references:
        if not is_numeric_dtype(df[col_name]):
            return pd.DataFrame()
    
    # Create a copy of the DataFrame to avoid modifying the original
    result_df = df.copy()
    
    # Evaluate the expression and add the new column
    try:
        # Use pandas eval for safe expression evaluation
        result_df[new_column] = result_df.eval(role_cleaned)
    except Exception:
        # If evaluation fails for any reason, return empty DataFrame
        return pd.DataFrame()
    
    return result_df


def _is_valid_column_name(column_name: str) -> bool:
    """Validate that a column name contains only letters and underscores."""
    pattern = r'^[a-zA-Z_]+$'
    return bool(re.match(pattern, column_name))


def _extract_column_names(expression: str) -> list:
    """Extract all potential column names from a mathematical expression."""
    pattern = r'[a-zA-Z_]+'
    matches = re.findall(pattern, expression)
    
    # Return unique column names preserving order
    seen = set()
    unique_matches = []
    for match in matches:
        if match not in seen:
            seen.add(match)
            unique_matches.append(match)
    
    return unique_matches


def _is_valid_expression(expression: str) -> bool:
    """Validate expression grammar: name (op name)* with allowed operators only."""
    if "**" in expression:
        return False
    pattern = r'^\s*[A-Za-z_]+(\s*[\+\-\*]\s*[A-Za-z_]+)*\s*$'
    return bool(re.match(pattern, expression))
