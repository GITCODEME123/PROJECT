import pytest
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal


@pytest.fixture
def sample_data():
    """Provides sample data for testing."""
    return pd.DataFrame(
        {
            "Group": ["A", "B", "A", "B", "A", "B"],
            "eTIV": [1400, 1500, 1450, 1550, 1425, 1525],
            "nWBV": [0.7, 0.75, 0.71, 0.76, 0.72, 0.77],
            "ASF": [0.9, 0.85, 0.88, 0.86, 0.89, 0.87],
        }
    )


def test_compare_groups(sample_data):
    """Test the compare_groups function for accurate statistics calculation."""
    
    from data_analysis import compare_groups

    # Test for eTIV metric
    etiv_result = compare_groups(sample_data, "eTIV")
    
    # Check basic structure
    assert isinstance(etiv_result, pd.DataFrame)
    assert list(etiv_result.columns) == ["mean", "min", "max", "median"]
    assert list(etiv_result.index) == ["A", "B"]
    
    # Verify all statistics for eTIV - Group A
    assert etiv_result.loc["A", "mean"] == pytest.approx(1425.0)
    assert etiv_result.loc["A", "min"] == 1400.0
    assert etiv_result.loc["A", "max"] == 1450.0
    assert etiv_result.loc["A", "median"] == 1425.0
    
    # Verify all statistics for eTIV - Group B
    assert etiv_result.loc["B", "mean"] == pytest.approx(1525.0)
    assert etiv_result.loc["B", "min"] == 1500.0
    assert etiv_result.loc["B", "max"] == 1550.0
    assert etiv_result.loc["B", "median"] == 1525.0
    
    # Test for nWBV metric
    nwbv_result = compare_groups(sample_data, "nWBV")
    
    # Verify all statistics for nWBV - Group A
    assert nwbv_result.loc["A", "mean"] == pytest.approx(0.71)
    assert nwbv_result.loc["A", "min"] == 0.70
    assert nwbv_result.loc["A", "max"] == 0.72
    assert nwbv_result.loc["A", "median"] == 0.71
    
    # Verify all statistics for nWBV - Group B
    assert nwbv_result.loc["B", "mean"] == pytest.approx(0.76)
    assert nwbv_result.loc["B", "min"] == 0.75
    assert nwbv_result.loc["B", "max"] == 0.77
    assert nwbv_result.loc["B", "median"] == 0.76
    
    # Test for ASF metric
    asf_result = compare_groups(sample_data, "ASF")
    
    # Verify all statistics for ASF - Group A
    assert asf_result.loc["A", "mean"] == pytest.approx(0.89)
    assert asf_result.loc["A", "min"] == 0.88
    assert asf_result.loc["A", "max"] == 0.90
    assert asf_result.loc["A", "median"] == 0.89
    
    # Verify all statistics for ASF - Group B
    assert asf_result.loc["B", "mean"] == pytest.approx(0.86)
    assert asf_result.loc["B", "min"] == 0.85
    assert asf_result.loc["B", "max"] == 0.87
    assert asf_result.loc["B", "median"] == 0.86


def test_compare_groups_empty_data():
    """Test compare_groups function with empty DataFrame."""

    from data_analysis import compare_groups

    empty_df = pd.DataFrame(columns=["Group", "eTIV", "nWBV", "ASF"])
    with pytest.raises(ValueError):
        compare_groups(empty_df, "eTIV")


def test_compare_groups_invalid_metric(sample_data):
    """Test compare_groups function with invalid metric name."""

    from data_analysis import compare_groups

    with pytest.raises(KeyError):
        compare_groups(sample_data, "InvalidMetric")


def test_compare_groups_single_group(sample_data):
    """Test compare_groups function with single group."""

    from data_analysis import compare_groups

    single_group_df = sample_data[sample_data["Group"] == "A"].copy()
    result = compare_groups(single_group_df, "eTIV")
    
    assert len(result) == 1
    assert "A" in result.index
    assert "B" not in result.index


def test_compare_groups_null_values(sample_data):
    """Test compare_groups function with null values."""

    from data_analysis import compare_groups

    # Insert some null values
    df_with_nulls = sample_data.copy()
    df_with_nulls.loc[0, "eTIV"] = np.nan
    
    result = compare_groups(df_with_nulls, "eTIV")
    
    # Check that statistics are calculated correctly excluding null values
    assert not np.isnan(result.loc["A", "mean"])
    assert not np.isnan(result.loc["A", "median"])