import pandas as pd
from synthcity.plugins import Plugins
from synthcity.plugins.core.dataloader import GenericDataLoader

df = pd.read_csv("data/flat-training.csv").dropna()
categorical = df.select_dtypes(include='object').columns.tolist()
loader = GenericDataLoader(dataframe=df, categorical_columns=categorical)
plugin = Plugins().get("tvae")
plugin.fit(loader)
synthetic = plugin.generate(count=len(df)).dataframe()
synthetic.to_csv("data/your-flat-submission01.csv", index=False)
print("✅ Flat synthetic dataset generated.")
