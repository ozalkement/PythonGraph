import pandas as pd
import numpy as np
path='C:/Users/user/Desktop/vedat/titanic.csv'
df =pd.read_csv(path)
print(df.shape)
print(df.head())
print(df.tail())
print(df.info())
print(df.isnull().sum().sort_values(ascending=False))
print(df["Embarked"].value_counts())
df["Embarked"].fillna(df["Embarked"].mode()[0],inplace=True)
print(df["Age"].mean())
print(df["Age"].median())
df["Age"].fillna(df["Age"].mean(),inplace=True)
df.drop(["Name","PassengerId","Ticket","Cabin"],axis=1,inplace=True)
print(df)
print(df.isnull().sum())
