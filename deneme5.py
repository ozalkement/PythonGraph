import matplotlib.pyplot as plt
import pandas as pd
path='C:/Users/user/Desktop/vedat/titanic.csv'
df =pd.read_csv(path)
print(df.tail(10))
df=df.sort_values(by=["Age"])
plt.figure(figsize=(15,8))
plt.plot(df.Age,df.Fare,color="blue",linewidth=3)
plt.xticks(rotation=90)
plt.title("Yaşa Göre Ödenen fiyat ")
plt.xlabel("Fiyat")
plt.ylabel("Yaş")
plt.show()

