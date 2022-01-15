'''
lst1 = ["one", "two", "Three"]
lst2 = [1, 2, 3, 4]
dct = dict(zip(lst1, lst2))
lst3 = list(zip(lst1, lst2))
print(dct)

print(lst3)


#7
str1 = "hello"
str2 = "olleh"

if set(str1) == set(str2):
    print("Anagrama")
else:
    print("Anagramma emas")

#6
nums = map(int,input().split(","))
nums = set(nums)
print(nums)

#8
user = {
    "name":"Ali",
    "hobbe": {
        "sport":["Tennis", {"Futbol":"Uz"}],
        
        }
    
    }
print(user["hobbe"]["sport"][1]["Futbol"])


lst = [111,23,23,4,51,6,17,86,9]

#for i in lst:
#    print(i, end=" ")

for i in range(len(lst)):
    print(lst[i])

toq = []
juft = []
for i in lst:
    if i % 2 == 1:
        toq.append(i)
    else:
        juft.append(i)

print(toq)
print(juft)



toq = [i for i in lst if i % 2 == 1]
print(toq)
juft = [i for i in lst if i%2 == 0]
print(juft)




str1 = "Python developer"
#for char in str1:
 #   print(char, end="")



for i in range(len(str1)):
    print(str1[i])


k =     False
s = [1,1,1,2,2,2,3,3,3,4,4]
for i in set(s):
   if i == 454:
       k = True
       break
print(k)
'''

user = {
    "name":"Username",
    "pass":"*******",
    "email":"",
    "tel":"",
    "addrss":""
    }
'''
for key in user:
    print(key)

for key in user.keys():
    print(key)

for val in user.values():
    print(val)

for key, val in user.items():
    print(key, val)


for key in user:
    if user[key] == "":
        user[key] = input(f"{key} ma'lumotingizni kiriting: ")

print(user)

    

#for1

n, k = map(int, input().split())
for i in range(n):
    print(k)

#for3

a , b = map(int, input().split())
for i in range(b-1, a, -1):
    print(i)

for i in reversed(range(a+1,b)):
    print(i)

#for 14

n = int(input())
summa = 0
for i in range(1, 2*n, 2):
    summa += i

print(summa)
    


#for20

n = int(input())
s = 0
p = 1
for i in range(1,n+1):
    p *= i
    s += p
print(s)

'''
for i in range(1,10):
    for j in range(1,10):
        print(f"{i} * {j} = {i*j}")
    print()



    
