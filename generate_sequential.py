import pandas as pd
from synthcity.plugins import Plugins
from synthcity.plugins.core.dataloader import TimeSeriesDataLoader

df = pd.read_csv("data/sequential-training.csv").dropna()
group_col = df.columns[0]
categorical = df.select_dtypes(include='object').columns.drop(group_col).tolist()
loader = TimeSeriesDataLoader(
    dataframe=df,
    categorical_columns=categorical,
    target_column=None,
    time_column=None,
    static_columns=[],
    index_column=group_col,
)
plugin = Plugins(category="sequential").get("ddpm_seq")
plugin.fit(loader)
synthetic = plugin.generate(count=len(df)).dataframe()
synthetic.to_csv("data/your-sequential-submission01.csv", index=False)
print("✅ Sequential synthetic dataset generated.")
