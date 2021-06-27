# dict = {k1:v1...}
employee ={
    'id': 45289,
    'name': 'John',
    'height': 6.5,
    'languages': ['English', 'spanish', 'hindi',['Python', 'C', 'Java']],
    'add' : ('res', 'off'),
    'M':True,
    'education' : {'UG','PG'},
    'comp' : 4 +5j,
                   
}
print(employee['languages'][1])  # -> employee['languages']  ---> ['English', 'spanish', 'hindi'] [1]
print(employee['languages'][3][1])  
# -> employee['languages']  ---> ['English', 'spanish', 'hindi',['Python', 'C', 'Java']] [3] --->['Python', 'C', 'Java'][1]
#1,2   3,2    3,1 ,      2,1
#print(employee['comp'])

#print(employee['m']) # KeyError: 'm'
#print(employee.get('m')) # None when key doesnt exist but not an error.
#print("continue")

print(employee.keys()) # dict_keys(['id', 'name', 'height', 'languages', 'add', 'M', 'education', 'comp'])
#print(employee.add(5))
employee[5] = 'new value'
print(employee)


dictex = {1:11,
          2:22,
          3:33,
}

print("before")
print(dictex)
print("after")

dictex[2] = 44 # add a new element or item to an existing dictionary
print(dictex)

dictex[4] = 55
print(dictex)
dictex[6] =66
print(dictex)

print(dictex.keys()) #dict_keys([1, 2, 3, 4, 6])
listx = dictex.keys()
print(type(listx))  # <class 'dict_keys'>
print(dictex.values()) # dict_values([11, 44, 33, 55, 66])


print("final-----")

listy = [(0,), (1,), (2,)] # (1,) -? A tupe with single element.

print(listy)
print(type(listy))

newlist = dict(listy) 
print(newlist)#{0: 'Zero', 1: 'One'}
print(type(newlist)) #<class 'dict'>
# ValueError: dictionary update sequence element #0 has length 1; 2 is required
# error,

# {0:''
# 1:?? }

# Assig: figure out how to concatenate two dictionaries
dict1 = {
    1:11,
    2:22,    
}

dict2= {
    3:33,
    4:44,
}

#print(dict1 + dict2) #ValueError: dictionary update sequence element #0 has length 1; 2 is required
