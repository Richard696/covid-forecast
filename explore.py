import pandas as pd 

df = pd.read_csv("saudi_covid_who.csv")
# print(df.head(5))

# df["date"] = df.Date.astype(str)
print(df.date.dtypes)

