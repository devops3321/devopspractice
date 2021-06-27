dict1 = {1:11,
         2:22,
         3:33,
}

print("before")
print(dict1)
""" 
print("after clear")
dict1.clear()
print(dict1) """

""" del dict1
print("after del")
print(dict1) """

""" a=5
del a
print(a) """

#dict1.pop(2)
#print(dict1)

print("beofre popitem")
print(dict1)
dict1.popitem()
print(dict1)


dict2 = {
    11:1111,
    22:2222,
    
}

print(dict2)
# 1 way to add 
dict2[33]=3333
print(dict2)

#any other way - to add elements. update()
dict2.update({44:4444})
print(dict2)

for x in dict2:
    print(x)
    




