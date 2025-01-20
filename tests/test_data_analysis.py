import pytest
import pandas as pd
from src.data_analysis import compare_groups, save_group_comparisons


@pytest.fixture
def sample_data():
    """Provides sample data for testing."""
    return pd.DataFrame(
        {
            "Group": ["A", "B", "A", "B"],
            "eTIV": [1400, 1500, 1450, 1550],
            "nWBV": [0.7, 0.75, 0.71, 0.76],
            "ASF": [0.9, 0.85, 0.88, 0.86],
        }
    )


def test_compare_groups(sample_data):
    """Test the compare_groups function for accurate statistics calculation."""
    result = compare_groups(sample_data, "eTIV")
    assert result.loc["A", "mean"] == 1425
    assert result.loc["B", "min"] == 1500
    assert result.loc["B", "max"] == 1550
    assert result.loc["A", "median"] == 1425
