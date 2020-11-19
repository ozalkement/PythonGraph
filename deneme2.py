
import numpy as np
liste=[1,2,3,4,5,6,7,8]
list2=np.array([(1,2,3,4),(5,6,7,8),(9,10,11,12)])
print(list2.shape)
print(list2.size)
list3=np.arange(10)
print(list3)
list3=list3.reshape(2,5)
print(list3)
rn=np.random.randint(20, 70,15)
rn=rn.reshape(5,3)
print(rn)
print("Aritmaitk ortalama:\t", np.mean(rn))
print("Medyan :\t\t", np.median(rn))
print("Varyans :\t\t", np.var(rn))
print("Standart Sapma:\t\t", np.std(rn))