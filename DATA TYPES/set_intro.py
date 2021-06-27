# Set is a collection of data which is unordered and unindexed. No duplicate numbers
# {} 
setex = {1,2} 
print(type(setex)) 
setex = {1,2,'Ankit',1,2,3,4}
print(setex) # {1, 2, 3, 4, 'Ankit'}, {1, 2, 3, 'Ankit', 4}
# print(setex[4]) # TypeError: 'set' object is not subscriptable. Or in other words it means indexing does not apply to sets.

print(6 in setex) # check if a value exists in a set.

set1 ={1,2,3,4,3,4}
set2 ={5,6,7}

# print(set1 + set2) # no concatenation - TypeError: unsupported operand type(s) for +: 'set' and 'set'

print(set1.union(set2)) # 1,2,3,4,5,6,7

# two ways to create a set
# a. ={1,2}
# b. a=set()

a=set()
print(type(a))

set1 = {1,4,5,7}
set2 = {5,6}

print(set1.union(set2))
print(set1 | set2)

print(set1.intersection(set2))
print(set1 & set2)

print(set1.difference(set2))

oldset = {1,4,5,6}
newset = oldset.add(10)
print(oldset)
newset = oldset
print(newset)

''' oldset.add(['Hello'])  # 
print(oldset) '''

oldset.add(True) # T is stored as 1, and F is stored as 0
print(oldset)

''' oldset.discard(15)
print(oldset)

oldset.remove(15)
print(oldset) '''

oldset.pop()
print(oldset) # 

#del oldset
#print(oldset)

# frozenset - immutable version of set
''' x = frozenset([1,2,3,4])

print(x)
print(type(x)) '''




