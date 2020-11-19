import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
path='C:/Users/user/Desktop/vedat/titanic.csv'
df =pd.read_csv(path)
print(df.Age)
print(df.info())
print(df.dtypes)
print(df.size)
print(df.shape)
print(df.describe().T)
print(df.isnull().sum())
df =df.dropna()
print(df.isnull().sum())
print(df.size)
#df = df.head(10)

#sns.scatterplot(x=df.Age,y=df.Fare)
#sns.countplot(x=df.Sex)

#a=sns.barplot(x="Sex",y="Survived",hue="Sex",data=df)
#a.set_title("Cinsiyete Göre Hayatta Kalma")

#sns.pairplot(df)

#corr=df.corr()
#plt.figure(figsize=(8,8))
#a=sns.heatmap(corr,vmax=.99,linewidths=0.5,square=True,annot=True,linecolor="black")

#sns.countplot(x=df.Sex)

sns.catplot(x="Pclass",kind="count",hue="Sex",palette="Set1",data=df)

plt.show()
