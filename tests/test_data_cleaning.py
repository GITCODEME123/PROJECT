import pytest
import pandas as pd
import numpy as np


def test_clean_data_missing_columns():
    """Test that clean_data raises ValueError when required columns are missing"""
    # Create sample DataFrame missing required columns
    df = pd.DataFrame(
        {"Group": ["A", "B"], "eTIV": [1400, 1500]}  # Missing nWBV and ASF
    )

    with pytest.raises(ValueError) as exc_info:
        from data_cleaning import clean_data

        clean_data(df)

    assert "Missing required columns" in str(exc_info.value)


def test_clean_data_handles_missing_values():
    """Test that clean_data properly handles missing values"""
    # Create sample DataFrame with missing values
    df = pd.DataFrame(
        {
            "Group": ["A", "B", "A", "B"],
            "eTIV": [1400, np.nan, 1600, 1500],
            "nWBV": [0.7, 0.75, np.nan, 0.72],
            "ASF": [0.9, 0.85, 0.88, np.nan],
        }
    )

    from data_cleaning import clean_data

    cleaned_df = clean_data(df)

    # Check that there are no missing values in the cleaned DataFrame
    assert cleaned_df.isnull().sum().sum() == 0


def test_clean_data_returns_required_columns():
    """Test that clean_data returns only the required columns"""
    # Create sample DataFrame with extra columns
    df = pd.DataFrame(
        {
            "Group": ["A", "B"],
            "eTIV": [1400, 1500],
            "nWBV": [0.7, 0.75],
            "ASF": [0.9, 0.85],
            "extra_col": [1, 2],
        }
    )

    from data_cleaning import clean_data

    cleaned_df = clean_data(df)

    # Check that only required columns are present
    assert set(cleaned_df.columns) == {"Group", "eTIV", "nWBV", "ASF"}
