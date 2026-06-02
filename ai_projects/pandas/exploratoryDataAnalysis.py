import pandas as pd
df=pd.read_csv(r"ai_projects\pandas\emp_sample.csv")
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.sort_values("Salary"))
print(df.sort_values("Salary",ascending=False))