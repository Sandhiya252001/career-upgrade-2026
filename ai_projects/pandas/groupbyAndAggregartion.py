import pandas as pd
df=pd.read_csv(r"ai_projects\pandas\emp_sample.csv")
print(df.groupby("Department")["Salary"].mean()) #Average of salary
print(df.groupby("Department")["Salary"].sum()) #Sum of salary
print(df.groupby("Department").size()) #count of employees