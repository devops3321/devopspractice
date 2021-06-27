# heterogeneous DT - if you want to store multiple types of data into one var -> list
# list - is a combination of numbers, strings and even other DT
# how to create a list  -> []
# so if [] is used against a string or string var eg Ankit[3] - then this is index of the var or string.
# but if its used =[] then its called a list. or in other words this is how you def a list. listvar = [<values>]

x=5
y=8.76

listNum = [1,2,3,4,5] #defining a list
print(type(listNum)) #<class 'list'>
print(listNum) #whole list
print(listNum[3]) #

listx = [1,2.76,3,4.89,5,'ankit','Satya', 'Aftab']
print(listx)
#print(listx[8]) # IndexError: list index out of range
print(listx[6]) #Satya
print(listx[3]) #4.89

evenList = [2,4,6,8,10]
oddList =  [1,3,5,7,9]
total = evenList + oddList
print (total) # [3,7,11...], [21,43,65,....], correct - [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
# joined -concatenate 
print(total[4]) #10
print(type(total[4])) # class int. ........ print(type(10)) ---> print(<clas int>) -> <class int

x=2
print(type(x))
# definition - how u define a var - and implicitly(py) ur var gets assigned a type (class <>)

# lists within lists.
person = ['John', 45,200.45, ['French', 'Spanish', 'English']]

''' temp=person[3]# ['French', 'Spanish', 'English'][1] -> temp[1]
print(temp[1]) '''

print(person[3][1])

person[3][1] = 'German'

print(person)
''' german =person

print(german)
x=2
y=x
print(x) '''

langSpoken = ['French', 'Spanish', 'English']
proglang = ['C', 'C++', 'Python', 'Java']

person2 = ['John', 45,200.45, langSpoken, proglang, True]
print(person2) # ['John', 45, 200.45, ['French', 'Spanish', 'English'], ['C', 'C++', 'Python', 'Java'], True]

person3 = ['John', 45, 200.45, ['French', 'Spanish', 'English'], ['C', 'C++', 'Python', 'Java'], True]
print(person3)
print(person3[4][2]) # Python

person4 = ['John', 45, 200.45, ['French', 'Spanish', 'English', ['C', 'C++', 'Python', 'Java']], True]
print(person4)
print(person4[3][3][2]) #Python   
# person4[3] -> ['French', 'Spanish', 'English', ['C', 'C++', 'Python', 'Java']]
# person4[3][3] ----> ['French', 'Spanish', 'English', ['C', 'C++', 'Python', 'Java']][3] -> ['C', 'C++', 'Python', 'Java']
# person4[3][3][2] ---> ['C', 'C++', 'Python', 'Java'] [2] --> Python


# Iterable - 'Ankit'
evenList = [2,4,6,8,10]
oddList =  [1,3,5,7,9]
total = evenList + oddList

