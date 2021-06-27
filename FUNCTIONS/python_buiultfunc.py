''' x = -45
# abs() - absoulte value.
print(abs(x)) '''

# all() and any()
# True - 1, False - 0
listx = [1,2,3,4.89,5,12,True,'hello','Vijay',None]
print(all(listx))

listy = []
print(all(listy))

# all() ---> will be false for only and any of these 3 ----->0, False, None

# any() ---> only for none value alone or empty then only false.
setz = {None,None,None}
print(any(setz))
print(any(listy))


# sum()
listeg = {1,2,3,4,4,3,1}
print(sum(listeg))

''' print("====here=====")
listeg1 = 'ankit'
print(sum(listeg1))
 '''

print(sum(listeg,2))

# dir() -> directory 

print(dir())
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'listeg', 'listx', 'listy', 'setz']

#enumerate - it adds a counter

colors = ('red','green','blue')
e=list(enumerate(colors))
print(e) #  [(0, 'red'), (1, 'green'), (2, 'blue')]

''' x=2
e1=list(enumerate(x))
print(e1) '''

compvar = 5+8j # j is sqrt of -1 -> irrational number
print(abs(compvar))

edict=dict(e) # {0: 'red', 1: 'green', 2: 'blue'}
newenumerate=dict(enumerate(edict)) # -> [(0, 0), (1, 1), (2, 2)]
print(newenumerate)  # {0: 0, 1: 1, 2: 2}

dict2 = {
    'a': 10,
    'b': 20,
       
}

print(dict(enumerate(dict2)))
# {0: 'a', 1: 'b'}


colors = ('red','green','blue')
e=list(enumerate(colors,90))
print(e) #  [(0, 'red'), (1, 'green'), (2, 'blue')]
print(enumerate(colors)) #  enumerate object at 0x01DAA0A8>

print("=====with for loop=====")
for index,itemanem in enumerate(colors):
    print(index,itemanem)