import pandas as pd
import numpy as np


class PandasJob:
    def __init__(self):
        pass

    def create_sample_df(self) -> pd.DataFrame:
        """Create a dataframe."""
        df = pd.DataFrame(
            data={"a": np.arange(0, 10000), "b": np.arange(0, 10000)},
            columns=["a", "b"],
        )
        df["datetime"] = pd.date_range(
            start="2020-03-15 7:00:00", periods=10000, freq="15min"
        )
        df["date"] = pd.date_range(
            start="2020-03-15 7:00:00", periods=10000, freq="15min"
        ).strftime("%Y-%m-%d")
        return df

    def write_csv(self, df, dir="output") -> None:
        """Write CSV"""
        df.to_csv(f"./{dir}/sample_dataframe.csv", index=False)
