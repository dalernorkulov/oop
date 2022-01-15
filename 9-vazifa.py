'''#1
def ism(name):
   
    print(f"Salom {name}")


ism('Daler')

#2
def lx(*ismlar):
    return max(ismlar, key = len)

print(lx('Daler','Laziz','Habibulloh'))
#3
def lx(*ismlar):
    return min(ismlar, key = len)

print(lx('Daler','Laziz','Habibulloh'))
#4
n = str(input("Ism kiriting:"))
def rev_name(n):
    print(n[::-1])

rev_name(n)
#5
a,b = map(int, input("Ikkita son kiriting:").split())
def max_num(a,b):
    if a == b:
        return "Sonlar teng"
    return max(a,b)

print(max_num(a,b))
#6
n = int(input("Son kiriting:"))
def qoldiq_tek(a):
    for i in range(2,11):
        if a % i == 0:
            print(f"{a} soni {i} ga qoldiqsiz bo`linadi.")
        else:
             print(f"{a} soni {i} ga qoldiqsiz bo`linmaydi.")

qoldiq_tek(n)
#7
i = str(input("Ism:"))
f = str(input("Familiya:"))
ty = int(input("Tug'ilgan yil:"))
tj = str(input("Tug'ilgan joy:"))
e = str(input("e-mail:"))
tr = str(input("Tel raqam:"))
def anketa(**dct):
    
    print(dct)
    

anketa(Ism=i,Familiya=f,Tugilgan_yil=ty,Tugilgan_joy=tj,email=e,tel_raqam=tr)
#8
rad = float(input("Radiusni kiriting:"))
lst1 = ['Radiusi','Diametri','Uzunligi','Yuzasi']
def aylana(r):
    r = rad
    d = 2*rad
    l = 2*3.14*rad
    s = 3.14*rad**2
    lst2 = [r,d,l,s]
    dct = dict(zip(lst1,lst2))
    return dct

print(aylana(rad))
#9
import math
def kupaytma(*nums):
    
    print(math.prod(nums))

kupaytma(1,2,3,4)
#10
n = int(input("Son kiriting:"))
def faktorial(n):
    """Bu funksiya n ning faktorialini hisoblaydi"""
    s = 1
    for i in range(1,n+1):
        s *= i
    return s

print(faktorial(n))'''