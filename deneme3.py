import pandas as pd
import numpy as np
#seri=pd.Series([10,20,30,40,50,60,70,])

data = np.array([10,20,30,40,50,])
seri=pd.Series(data,index=[100,101,102,103,104])
print(seri)
yd={'a':0,'b':1,'c':2}
ys=pd.Series(yd)
print(ys)
print(ys[0:2])
print(ys[0:])
print(ys["b"])
print(ys[["a","b","c"]])
print(ys["a":"d"])
ys["a"]=90
print(ys)
print("Toplamı: ",ys.sum())
print("Maks: ",ys.max())
print("Ortalama: ",ys.mean())
print("Medyan: ",ys.median())
isimler=["Ali","Ömer","Ayşe","Hakkı","Zeynem"]
df=pd.DataFrame(isimler,columns=["İsimler"])
print(df)
plaka={"Şehirler":["Ankara","Bursa","Denizli","Eskişehir"],
       "plakkalar":[6,16,20,26]}
dp=pd.DataFrame(plaka,index=["a","b","c","d"])
dp["Havadurumu"]=pd.Series([33,25,45,26],index=["a","b","c","d"])
#dp.drop("Havadurumu",axis=1,inplace=True)
#dp.drop("a",axis=0,inplace=True)
print(dp)
print(dp.loc["b":"c"])
print(dp.iloc[1:3])
print("Toplam: ",dp['plakkalar'].sum())
print(dp.describe())
print(dp[dp.Havadurumu>30]["Şehirler"])