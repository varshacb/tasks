import pandas as pd

df = pd.read_csv("salary_data.csv")

X = df.iloc[:,:-1].values
Y = df.iloc[:,0].values 
print(X)