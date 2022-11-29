import pandas as pd
import numpy as np
import pytest

from pipeline.pandas import PandasJob

# Fixtures


@pytest.fixture
def sample_df() -> pd.DataFrame:
    """Sample Dataframe Fixture"""
    job = PandasJob()
    df = job.create_sample_df()
    return df


@pytest.fixture(params=[-1, -2, -3])
def sample_param_df(request) -> pd.DataFrame:
    """Sample Dataframe Fixtur (Parameterized)"""
    job = PandasJob()
    df = job.create_sample_df()
    df["new_value"] = request.param
    return df


# Tests Types
# - column names
# - column dtypes


def test_sample_df_columns(sample_df: pd.DataFrame) -> None:
    """Test Columns"""
    expected_columns = ["a", "b", "datetime", "date"]
    actual_columns = list(sample_df.columns)
    assert actual_columns == expected_columns, "columns names do not match."


def test_sample_df_new_column(sample_param_df: pd.DataFrame) -> None:
    """Test New Column Datatype"""
    assert (
        sample_param_df["new_value"].dtype == np.int64
    ), "new column is not correct dtype"
