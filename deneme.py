number=[111,7,2,1]
print(number[-1])
print(number[-2])
print(number[:-4])
number.append(12)
number.insert(2,22)
print(number)
print(len(number))
mylist=[]
for i in range(20):
    mylist.append(str(i)+" aa")
print(mylist)
print(number)
number2=number[:]
number2[0]=33
print(number2)
print(7 in number2)
yenilist=[x  for x in range(25) if x %2==0]
print(yenilist)
empty="."
board= [[empty for i in range(8)] for j in range(8)]
print(board)
tup=(1,2,3)
print(tup[2])
t1=1.,2.,.3
print(t1)
t2=1,2,100,1000,100
print(t2[:-2])
t3 = t1+t2
print(100 not in t3)
print(t3.count(100))
print(len(t3))
dictionary = {"cat" : "kedi", "dog" : "köpek", "horse" : "at"}
for key in sorted(dictionary.values()):
    print(key)
dictionary.update({"deneme":"try"})
dictionary["yeni"]="new"
del dictionary["cat"]
for e,t in dictionary.items():
    print(e,t)
dictionary.popitem()
dictionary.popitem()
print(dictionary)
if "köpek" in dictionary.values():
    print("var")
else:
    print("yok")
yd=dictionary.copy()
dictionary.clear()
print(dictionary)
print(yd)
kume=set()
kume={2,2,3,3,6,5,8,5,5,5,}
print(len(kume))
for i in kume:
    print(i)
def karekok():
        print(12**0.5)
karekok()
def karekok(deger):
    return deger**0.5
var= karekok(144)
print(var)
def birlestir(bir,iki,ayrac):
    print(bir,iki,sep=ayrac)
birlestir("Özal",   "kement","-")
def karebul(i):
    cikti="{} saysıısnın  karesi {}"
    print(cikti.format(i,i**2))
    print(f"{cikti}")
karebul(5)
birlestir(iki="Kement",bir="Özal",ayrac="***")
def fok(*par):
    for i in par:
        print(i*i)
fok(1,2,3,4,4)
print(*"TBMM",sep=".")
def fok3(**par):
    print(par)
fok3(isim="Özal", soyisim="kement")
import random
def sayiuret(baslangic=0,bitis=500,adet=6):
    sayilar=set()
    while len(sayilar)<adet:
        sayilar.add(random.randrange(baslangic,bitis))
    return sayilar
print(sayiuret(0,10,3))
liste=["ahmet","mehmet","veli","ayşe","zeynep"]
print(random.sample(liste,2))
random.shuffle(liste)
print(liste)

isim = "Mimar"
def f():
    global isim
    isim += " Sinan"
    return isim
print(f())


try:
    x=1/0
except ZeroDivisionError as hata:
    print("Sıfıra bölme hatası", hata)
except ValueError:
    print("Değer hatası")
except FloatingPointError:
    print("floatin point")
except:
    print("fdfd")
raise Exception("Hata oldu")
    