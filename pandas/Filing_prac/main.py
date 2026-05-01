import pandas as pd

df = pd.read_csv("pokemon.csv")

#Data cleaning

# #Drop a column
# df = df.drop(columns=["Height"])

# Handling missing data
df = df.dropna(subset=["Type2"])
print(df)



##Agreegation
# print(df.mean(numeric_only=True))
