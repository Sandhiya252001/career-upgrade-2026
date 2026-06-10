import pandas as pd
df=pd.read_csv(r"C:\Users\sandhiya.c.subramani\Desktop\Python\Day 01\career_upgrade_2026\ai_projects\pandas\erroranddays.csv")
print(df["Errors"].mean())
print(df["Errors"].std())
import matplotlib.pyplot as plt
plt.boxplot(df["Errors"])
plt.show()