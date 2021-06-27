# List is a collection of data which is ordered and changeable. Allows duplicate numbers
# Tuple is a collection of data which is ordered and unchangeable. Allows duplicate numbers
# Set is a collection of data which is unordered and unindexed. No duplicate numbers
# tuple are imutable.
# tuples contain static data
# lists contain dynamic data

# =[]
# =() - create a tuple
# tuple() - also to create a tuple

tuplex = (11,22,33,44)
print("length of tuple is " , len(tuplex))
# print(tuplex)
# print(type(tuplex))

# indexing works the same way as in lists or strings.
print(tuplex[2])
print(tuplex[-3])

#tuplex[1] = 9 # tuples are imutable
#print(tuplex)

tuplex1 = ('Noida', "Hyderabad", 'Delhi', 'Mumbai', 'Agra', 'Calcutta')
print(tuplex1[-4:-1]) # D,M,A... C,A,M,D.....D,M,A,C....D,A,C ..... C,A,M
print(tuplex1[-1:-4]) # empty

# diff betwen num = (1) and num=(1,)
numbers=(1,)
print(type(numbers)) #Tuple with a single element.

names=('ankit',)
print(type(names))

# Assign:Is there a way to change the values of a tuple. how?
# ANS: convert it to a list
x = ('1',2,3,4) #' ' "  " ''' '''
#x[3] = '6' # tuple are immutable
print("Original value of x")
print(x)
y = list(x)
print("-----")
print(x)
print(y)
y[3] = '6'
print("After conversion value of x")
x=tuple(y)
print(y)
print(x)

print("Before del")
listx =(1,2,3,4)
a=5
print(listx,a)

#print("After del")
#del listx,a
#print(listx,a)


a,b,c=2,3,4
print(a)
print(b)
print(c)
# ValueError: too many values to unpack (expected 2)
# packing and unpacking of variables

# packing into a var means adding values to a var
fruits = ('grapes', 'bannana', 'cherry')
# unpacking means assiging these values to variables

(green,yellow,red) = fruits # fruits -->  ('grapes', 'bannana', 'cherry')
#(1,2,3) = fruits # fruits -->  ('grapes', 'bannana', 'cherry')

print(green)
print(yellow)
print(red)

# (variables) = (values). no of variabels shud match no of values.
fruits1 = (1,2,3)
(green,yellow,red) = fruits1

print(green)
print(yellow)
print(red)

fruitsnew = ('grapes', 'bannana', 'cherry','apple','papaya','orange','kiwi', 'watermelon','bannana')

(green,*yellow,red) = fruitsnew 

print(green)
print(yellow)
print(red)

# in keyword
if ('melon' in fruitsnew):
    print (True)
else:
    print(False)

# loop thru a tuple
for i in fruitsnew:
    print(i)


# tuple methods - count and index
print(fruitsnew.count('bannana'))
#print(fruitsnew.index('melon')) 

# assign: how to find the index of ssecond occurence.

tuple1 = ('a','b','c')
tuple2 = (1,2,3)
tuple3 =  tuple1 + tuple2
print(tuple3)

outtuple = tuple1 * 3
print(outtuple) #

''' emptyTumple = []
for i in tuple2:
    print(i*2) # (2,4,6)
    emptyTumple.append(i*2)

print(tuple(emptyTumple)) '''
    
listy = [11,23,56,48,90]
listy.sort() # -> [11,23,48,56,90]
print(listy[::-1][1]) # error, None, 56, 48. # [90,56,48,23,11][1] -> 48
