import matplotlib.pyplot as plt
import pandas as pd
path='C:/Users/user/Desktop/vedat/titanic.csv'
df =pd.read_csv(path)
print(df.tail(10))
df.drop("PassengerId",axis=1,inplace=True)
print(df.tail(10))
print(df.sample(10))
df=df.sort_values(by=["Age"])
#plt.scatter(df.Age,df.Fare,color="r",label="Ücret")
#plt.scatter(df.Age,df.Pclass,color="y",label="Sınıf")
#plt.legend()
ydf=df[df["Survived"]==1]
print(ydf)
#plt.show()
plt.figure(figsize=(15,6))
#plt.hist(df.Age,label="Sınıf")
#df.Age.plot.hist()
#df=df.head(20)
df.Survived.value_counts().plot.pie(autopct="%1.3f%%",figsize=(12,12))
plt.show()

