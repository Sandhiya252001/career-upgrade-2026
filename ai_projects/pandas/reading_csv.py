import pandas as pd
df = pd.read_csv(
    r"C:\Users\sandhiya.c.subramani\Desktop\Python\Day 01\career_upgrade_2026\ai_projects\pandas\emp_sample.csv"
)
print(df)
#head() will print a preview, for example if there are 10 records, it will print 1st 5/4 records
print(df.head())
#print shape eg:(6,4)(rows,columns)
print(df.shape)
#print column names(eg:Index(['Name', 'Age', 'Salary', 'Department'], dtype='str')S)
print(df.columns)
#finf average of salary
print(df["Salary"].mean())
#filter employee list whose age>25
print(df[df["Age"]>25])
#filter only IT employees
print(df[df["Department"]=="IT"])
