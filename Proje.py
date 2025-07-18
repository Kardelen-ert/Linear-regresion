import pandas as pd
df=pd.read_csv("Advertising Budget and Sales.csv")
df=df.iloc[:,1:len(df)]
df.head()