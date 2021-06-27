listx =[1,2,3,4]
listy = [5]
print(listx + listy)
#listx[3] = 5 
#print(listx) # overwrite 4 to 5
listx.append(5) # Append object to the "end" of the list.
print(listx)

listx.append(7) # Append object to the "end" of the list.
print(listx) # [1, 2, 3, 4, 5, 7]

# lists can be modified - mutablity  or in other words lists are mutable.

# insert()
listy=[4,5,6,7]
listy.insert(2,8) #[4, 5, 8, 6, 7]
print(listy)

#extend()
# it adds multiple elemts to an exsiting list
listz=[78,89,100]
listz.extend([66,55,44])
print(listz)

# Assign1: Extending a list from a given index
# hint: use insert and extend 

# pop() - remove the values. LIFO
listp = [11,22,33,44,55,66,77]
listp.pop() # will pop the last amount - LIFO
print(listp)

# over "WRITE"
# x= user input
listp = [11,22,33,44,55,66,77]
listp.pop(2) 
print(listp) # [11, 22, 44, 55, 66, 77] 

# remove()
listp.remove(44) 
print(listp) # [11, 22, 55, 66, 77]

# listp.remove(4) 
# print(listp) # error

#over writting
x=2
y=5
x=10
print(x) # 10

listab=[1,2,3,2,2,2,1]
listab.remove(2)
print(listab) # first, all 2's, last 2 value - always the first occurence.
listab.remove(2)
print(listab) # 

# Assin 2: Remove all the occurecences of multiple values.


print("orig list")
print(listab)

print("====")
print("reversed list")
listab.reverse()
print(listab)
''' listempty=[]
listempty.append(listab[4])
listempty.append(listab[3])
listempty.append(listab[2])
listempty.append(listab[1])
listempty.append(listab[0])
print(listempty) '''

print("Reversing again so orig list")
print(listab[::-1]) # -ve indexing works here in list too.

print("=====Copy vs '=' =======")
# copy vs =
listx1 = [1,2,3,4]
listx2 = listx1
print(listx1)
print(listx2)
listx3=listx1.copy()
print(listx3)

listx1[3] = 8
print(listx1)
print(listx2)
print(listx3)


# strings - are immutable
name = 'Hello'
print(name)
name[4] = 'w' # 0 -> w # TypeError: 'str' object does not support item assignment
print(name) # Hellw