"""
name = 'ITEG academy'
print(name,type(name))
adress = '''
SamDU Fizika fakulteti
yonida
'''

print(adress,type(name))

print(ord("A"))
print(ord("a"))
print(chr(65))
print(chr(127878))

name = 'ITEG academy'
print(len(name))
print(max(name))
print(min(name))
print(sorted(name))

name = 'ITEG academy'
#       01234567891011
print(name[-(len(name)-1)])
print(name[-1])
print(name[-2])

#belgilarni kesib olish
name = 'ITEG academy'
print(name[0:4])
print(name[:4])
print(name[5:])
print(name[5:12])
print(name[5:7])
print(name[0:4:2])
print(name[::2])
print(name[::-1])

#stringlar ustida amallar
first_name = 'Daler'
last_name = 'Norkulov'
age = 18
full_name_1 = "Mening ismim {}, Familiyam {}, yoshim {} da".format(first_name,last_name,age)
print(full_name_1)
about = f'Mening ismim {first_name} yosh {age}'
print(about)
name = 'Samarqand'
print(f'{name} '*5)

name = 'ITEG academy'
print(name.lower())
print(name.upper())
print(name.title())
print(name.capitalize())
"""
name = 'ITEG academy. bu dasturlash'
phone_number='973993450'
print(phone_number.isdigit())
print(name.split("."))
print(name.count("das"))
full_name = 'Daler Norkulov'
print(full_name.count("a"))
print(5/2)
print(5//2)
a=map(str,input.split())
print(a)