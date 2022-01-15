"""#1
def uch_son(a,b,c):
    return max(a,b,c)
    

print(uch_son(4,2,3))
#2
def tub(a,b):
    
    lst = []
    for i in range(a,b):
        s = 0
        for j in range(1,i+1):
            if i % j == 0:
                s += 1
        if s == 2:
            lst.append(i)
    return(lst)

print(tub(1,100))
#Natija:[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
#3
def b_year(age):
    return now_year - age

first_name = input('First name:')
age = int(input('Age:'))
now_year = int(input('Now year:'))
print("Birth year: ",b_year(age))
#Natija
'''First name:Daler
Age:18
Now year:2021
Birth year:  2003'''

#4
def fib(n):
    lst = [1,1]
    k = 2
    while len(lst) != n:
        lst.append(lst[k-2] + lst[k-1])
        k += 1
    return lst

print(fib(10))
#Natija:[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

#5
def degree(x,y):
    return x**y

x,y = map(int,input().split())
print(degree(x,y))

#6
def summa(*arr):
   return sum(arr) 

print(summa(1,2,5,7,4))

#7
def student(**data):
    return data

first_name = input('First_name:')
last_name = input('Last_name:')

print(student(First_name = first_name,Last_name = last_name,Tel_number = '+998973993450'))
#Natija:{'First_name': 'Daler', 'Last_name': 'Norkulov', 'Tel_number': '+998973993450'}

#8
def fac(number):
    if number == 1:
        return 1
    return number * fac(number-1)

print(fac(10))

#9
def quad_equa(a,b,c):
    d = (b**2 - 4 * a * c)**(1/2)
    if a == 0 :
        return "Bu kvadrat tenglama emas"
    elif d == 0:
        return -b/(2*a)
    
    return (((-b)+d)/(2*a), ((-b)-d)/(2*a))

print(quad_equa(1,-5,6))

#10
def bit(n):
    b = n/8
    mb = b/1024
    gb = mb/1024
    print(f"{n} bit = {b} bayt")
    print(f"{b} bayt = {mb} megabayt")
    print(f"{mb} megabayt = {gb} gigabayt")

n = float(input("Ma`lumot hajmini kiriting(bitlarda):"))
bit(n)
#11
def hour_min(s):
    min = (s % 3600)//60
    hour = s//3600
    print(F"{hour} soat {min} daqiqa")

hour_min(84180)
#Natija:23 soat 23 daqiqa
#12
def lower_upper(str):
    l = 0
    u = 0
    for i in str:
        if i.isupper():
            u += 1
    for i in str:
        if i.islower():
            l += 1
    print("Katta harflar soni:",u)
    print("Kichik harflar soni:",l)
lower_upper('Tezkor Tulki')
#13
lst = [1,1,2,2,2,2,3,4,5,5,5,5,5]
def lst_unique(arr):
    lst2 = []
    for i in arr:
        if i not in lst2:
            lst2.append(i)
    return lst2
print(lst_unique(lst))"""