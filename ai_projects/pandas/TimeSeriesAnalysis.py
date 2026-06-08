import pandas as pd
df=pd.read_csv(r"C:\Users\sandhiya.c.subramani\Desktop\Python\Day 01\career_upgrade_2026\ai_projects\pandas\timeAnderrors.csv")
df["Date"]=pd.to_datetime(df["Date"])
print(df["Date"])
import matplotlib.pyplot as plt
plt.plot(df["Date"],df["Errors"])
plt.show()