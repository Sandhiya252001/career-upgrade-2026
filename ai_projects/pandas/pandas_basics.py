import pandas as pd
#Series
s=pd.Series([10,20,30])
print(s)
print(s[0])
s1=pd.Series([11,12,35],index=["A","B","C"])
print(s1)
#DataFrame
data={"Name":["Sandhiya","Shrithika"],"Age":[25,20]}
df=pd.DataFrame(data)
print(df)
#count rows
print(len(df))
#get Columns
print(df.columns)
#access Column
print(df["Age"])
#access Row using loc
print(df.loc[0])

