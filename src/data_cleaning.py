def clean_data(df):
    """
    Cleans the provided DataFrame by performing the following steps:
    1. Checks for required columns and raises an error if any are missing.
    2. Drops rows with missing values in the required columns.
    3. Fills missing values in numeric columns with the column's mean.
    4. Returns a DataFrame containing only the required columns.

    Parameters:
        df (pd.DataFrame): The input DataFrame to be cleaned.

    Returns:
        pd.DataFrame: A cleaned DataFrame containing only the required columns.

    Raises:
        ValueError: If any required columns are missing in the input DataFrame.
    """
    print("Starting data cleaning process")

    # Define the list of required columns
    required_columns = ["Group", "eTIV", "nWBV", "ASF"]
    # List to track any missing columns
    missing = []

    # Check for missing required columns in the input DataFrame
    for col in required_columns:
        if col not in df.columns:
            missing.append(col)

    # Raise an error if there are missing required columns
    if missing:
        raise ValueError("Missing required columns: " + ", ".join(missing))

    # Drop rows with missing values in any of the required columns
    df = df.dropna(subset=required_columns)

    # Fill missing numeric values with the column's mean
    for col in required_columns:
        if df[col].dtype in ["float64", "int64"]:  # Check for numeric column types
            df[col] = df[col].fillna(df[col].mean())

    print("Data cleaning completed successfully")
    # Return the cleaned DataFrame with only the required columns
    return df[required_columns]
