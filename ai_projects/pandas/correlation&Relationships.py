import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\sandhiya.c.subramani\Desktop\Python\Day 01\career_upgrade_2026\ai_projects\pandas\dataset.csv")
print(df.corr(numeric_only=True))
df1=pd.read_csv(r"C:\Users\sandhiya.c.subramani\Desktop\Python\Day 01\career_upgrade_2026\ai_projects\pandas\emp_sample.csv")
plt.scatter(df1["Age"],df1["Salary"])
plt.show()