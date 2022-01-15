'''
#def4
def name_reverse(first_name):
    return first_name[::-1]

print(name_reverse("Abror"))


#def6
def num_div(num):
    for i in range(2,11):
        if num % i == 0:
            print(f"{num} {i} soniga qoldiqsiz bulinadi! ")
num_div(48)


#def9
def multiply(*nums):
    p = 1
    for i in nums:
        p *= i
    return p
p = multiply(1,2,3,4,5)
print(p)


#def2
def max_name(*names):
    return max(names, key=lambda x: x[2])

max_ = max_name("Alijon", "Alisher", "Bahodir", "Abror")
print(max_)


add = lambda a,b: a+b
print(add(1,2))

def add(a,b):
    return a+b
'''
'''
#10-dars
def fac(number):
    if number == 1:
        return 1
    return number * fac(number-1)

print(fac(3))
print(fac(5))

#3! = 1*2*3
#3! = 2! * 3
#3! = 1! *2* 3


    


lst = [11, 12, 3, 5, 7, 9, 2, 4, 6, 8]

def summa(arr):
    if len(arr) == 0:
        return 0
    return arr[-1] + summa(arr[:-1])

print(summa(lst))
    


lst = [1,1,2,2,2,2,3,4,5,5,5,5,5]
def lst_unique(arr):
    lst2 = []
    for i in arr:
        if i not in lst2:
            lst2.append(i)
    return lst2
        

print(lst_unique(lst))


def summa():
    global x
    number = x + 4
    print(number)

   
x = 2
print(x)
summa()



def lower_upper(string):
    pass

print(lower_upper("Bu Bizning 10 Dars"))


#massiv101
def summa(*lst):
    s = 0
    k = 0
    urta = sum(lst)/len(lst)
    for i in lst:
        if i < urta:
            s += i
            k += 1
    return s/k
print(summa(58,22, 17, 84, 50, 53))


#algo103

def summa(lst,a,b):
    return sum(lst[a-1:b])/len(lst[a-1:b])

n = int(input())
lst = list(map(int, input().split()))
k,m = map(int,input().split())
print(summa(lst[:n],k,m))



def input_int():
    return int(input())


n = input_int()
print(n, type(n))

'''
#algo104

def arr(lst):
    k = lst.index(min(lst))
    lst[k], lst[-1] = lst[-1], lst[k]
    return lst

print(arr([12,0,2,16, -1, 90]))





