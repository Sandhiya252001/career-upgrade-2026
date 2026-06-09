import pandas as pd
df=pd.read_csv(r"C:\Users\sandhiya.c.subramani\Desktop\Python\Day 01\career_upgrade_2026\ai_projects\pandas\errors.csv")
df["MovingAvg"]=df["Errors"].rolling(window=3).mean()
print(df["MovingAvg"])
import matplotlib.pyplot as plt
plt.plot(df["Month"],df["Errors"])
plt.plot(df["Month"],df["MovingAvg"])
plt.show()