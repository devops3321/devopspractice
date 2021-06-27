# m imp datatype and is an object of map.
# {}
# {K:V} combinationi oif key and valur pair. 
# dictex = {K1:v1, K2:v2 , K3:v3 ........Kn:Vn}
# A dict is a collection which is ordered, changeable, and does not allow duplicates.
# dict()


dictex ={'one':1, 'two':2, 'three': 3}
print(type(dictex))
print(dictex)

# keys are immutable while values are not.
# len will give u the length

print(len(dictex))

dictex ={'one':1, 'two':2, 'three': 3, 'one':4}
print(dictex)

dict1 ={
    'brand' : 'audi',
    'model' : 'q5',
    'year' : 2021,        
}

print(dict1)
print(dict1['model'])

print("=======")
dict2 = {(1,2,3): 'first',
         4:'second',
}

print(dict2)
print(dict2[(1,2,3)])

dict4 = {
    (1,) :'oneten',
    'name' : 'Satya'
}

print(dict4[(1,)])

a=(1,2,3,4,5,('ankit','Satya', 'aftab'))
print(a)
print(type(a))

dict5 = {
    a: 'onetwo',                    # (1,2,3,4,5,['ankit','Satya', 'aftab']) : 'onetwo'
    'country': 'USA',
    'name' : 'Mohan',
}

print(dict5[a])

dict6 ={
    'brand' : 'audi',
    'model' : 'q5', #modell
    'year' : 2021,        

}

if 'year' in dict6:
    print("exists")
else:
    print("does not exist")

# 3 v imp inbuilt functions. keys(), values(), and items()

print(dict6.keys()) # dict_keys(['brand', 'model', 'year'])
print(dict6.values()) # dict_values(['audi', 'q5', 2021])
print(dict6.items()) # dict_items([('brand', 'audi'), ('model', 'q5'), ('year', 2021)])

for item in dict6.items():
    print(item)

''' 
('brand', 'audi')
('model', 'q5')
('year', 2021)
'''

""" listx= dict6.keys()
print(listx) # [dict_keys(['brand', 'model', 'year'])] """

#dict6['model'] = 'modell' # modifying the value here
#print(listx)

print(dict6)

print("using for loop to chnge the key")
emptylist= []

for key in dict6.keys():
    emptylist.append(key)

emptylist[1] = 'modell'
print(emptylist)

# dict6['model'] = dict6['modell']

print(dict6)


# To convert two lists into a dictionary

list1 = ['ram', 'sham', 'suresh', 'mahesh']
list2 = [233,455,677,998]
list3 = dict(list(zip(list1,list2)))
print(list3)
dict1 = dict(list3)
print(dict1)




