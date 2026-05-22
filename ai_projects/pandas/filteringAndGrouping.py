import pandas as pd
df = pd.read_csv(
    r"C:\Users\sandhiya.c.subramani\Desktop\Python\Day 01\career_upgrade_2026\ai_projects\pandas\emp_sample.csv"
)
#filtering data
print(df[df["Department"]=="IT"])
print(df[df["Salary"]>50000])
#grouping
avg=df.groupby("Department")["Salary"].mean()
print(avg)
