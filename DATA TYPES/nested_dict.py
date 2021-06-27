# nested dict - dict within a dict
# {{}}

myFamily ={
    'child1': { 
     'name': 'John',
    'year': 1998,
    },
    'child2':{
        'name': 'Tony',
        'year': 2004,
    },
    'child3': {
        'name': 'TOM',
        'year': 2019,
    },
    
}

print("from the first method")
print(myFamily)
print(myFamily['child1']['name'])

""" child1 = { 
     'name': 'John',
    'year': 1998,
}

print(child1['name'])   """ 

#creat 1 dic that will contain 3 other dict using var.

print("======")
print("from the second method")
child1 = { 
    'name': 'John',
    'year': 1998,
    }
    
child2={
    'name': 'Tony',
    'year': 2004,
    }
    
child3= {
    'name': 'TOM',
    'year': 2019,
    }
    
myFamily ={
    'child1': child1,   
    ''' 'child1': { 
    'name': 'John',
    'year': 1998,
    } '''
    'child2': child2,
    'child3': child3,
}

print(myFamily['child1']['name'])


# fromkeys()
dictex = {
    1:11,
    2:22,
}

print("======fromkeys")
# dictex.fromkeys()
keys = ['A','B','C','D'] #list
emptyList = {}
#emptyList = emptyList.fromkeys(keys)
#print(emptyList)
#{'A': None, 'B': None, 'C': None, 'D': None}

values=89
emptyList = emptyList.fromkeys(keys,values)
print(emptyList)
#{'A': 89, 'B': 89, 'C': 89, 'D': 89}

# value is duplicate for all the keys.

print("====without empty")

z = dict.fromkeys(keys,values)
print(z)

# a={}
# dict() are same.


# Assign: Can we stop it from overriding the keys.
# eg

""" dictex = {
    1:11,
    2:22,
}

dictex[1]=44
print(dictex) """
