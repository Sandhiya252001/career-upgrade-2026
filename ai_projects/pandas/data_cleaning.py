import pandas as pd
df=pd.read_csv(r"C:\Users\sandhiya.c.subramani\Desktop\Python\Day 01\career_upgrade_2026\ai_projects\pandas\emp_sample.csv")
#1.checking missing values
missing_values=df.isnull()
print(missing_values)
#print(df.isnull())
#2.Count missing values
print(df.isnull().sum())
print(missing_values.sum())
#3.Fill Missing values
df.fillna(0)
print(df)
#Drop missing rows
dup=df.dropna()
print(dup)
#To drop original df
df.dropna(inplace=True)
print(df)