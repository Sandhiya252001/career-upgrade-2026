import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"ai_projects\pandas\errors.csv")
plt.plot(df["Month"],df["Errors"])
print(plt.show())
