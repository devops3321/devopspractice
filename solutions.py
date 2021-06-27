print("===========================================================")
# METHOD 1
dict6 = {'brand': 'audi', 'model':'q5', 'year':2021}
print("The original Dictionary is :", dict6)
dict6['modell'] = dict6['model']
del dict6['model']
print("The new updated dictionary is:", dict6)

print("===========================================================") 
#METHOD 2
dict6 = {'brand': 'audi', 'model':'q5', 'year':2021}
print("The original Dictionary is :", dict6)
dict6['modell'] = dict6.pop('model')
print("The new Dictionary is :", dict6)


print("===========================================================")
# Concatenation of dictionaries
emp = {
    'languages' : 'english',
    'id' : 23331,
    'age' : 23,
    
}

emp1 = {
    'salary' : 50000,
    'residence' : 'delhi',
    'relationshipstatus' : 'married'
}

empnew = (emp | emp1)
print(empnew)

print("===========================================================")

print("============satya's solution ==================")
# concatenation of dictionaries
dict1 ={1:11,
        2:22,
        3:33,
}

dict2={'a':'aa',
       'b':'bb',}

dict3={}

for key,value in dict1.items(): ### copying the dict1 into dict3
    #print(key,value)
    dict3[key]=value
print(dict3)


for key,value in dict2.items():  
    #print(key,value)
    dict3[key]=value   ### adding the keys and values of dict2 into dict3

print("printing below the concatenation of dictionaries dict1 and dict2")
print(dict3)  ### printing the concatenated value of dict1 and dict2

print("===========================================================")

# assignment 1
# Looping through the numbers from 1 to 10 and adding 50 to even and 25 to odd. 
for num in range(1,10):
       if num%2 == 0:
           #print("Number is even")
           num=num+50
           print(num)
       else:
        #print("Number is Odd")
        num=num+25
        print(num)

# assignment 2
# finding the largest number in a list using sort

lista = [224,345,678,902,381,529,1002]
lista.sort
print("largest no. is:", lista[-1])

print("===========================================================")

# assignemet 2 alternative using functions
# finding the largest number in a list using functions
def largest_no(list1):
    largest_no=list1[0]
    for count in list1:
        if count>largest_no:
            largest_no=count
    return largest_no
list1=[224,345,678,902,381,529,1002]
print("Largest no is: ",largest_no(list1))

print("===========================================================")

# assignment 3
seta={23,45,11,77,90}
sum=0
for iterVar in seta:
    sum=sum+iterVar
print(sum)

print("===========================================================")
# assignment 4
# 1st approach without using inbuilt string functions
string1= "I am learning Python 101 and I hope to finish by $#."
vowel=0
consonant=0
digit=0
specialChar=0
for char in string1:
    if char=='a'or char=='e' or char=='i' or char=='o' or char=='u' or char=='A'or char=='E' or char=='I' or char=='O' or char=='U':
        vowel=vowel+1
    elif char=='b'or char=='c' or char=='d' or char=='f' or char=='g' or char=='h'or char=='i' or char=='j' or char=='k' or char=='l' or char=='m'or char=='n' or char=='p' or char=='q' or char=='r' or char=='s'or char=='t' or char=='v' or char=='w' or char=='x' or char=='y'or char=='z' or char=='B' or char=='C' or char=='D' or char=='F'or char=='G' or char=='H' or char=='J' or char=='K' or char=='L'or char=='M' or char=='N' or char=='P' or char=='Q' or char=='R'or char=='S' or char=='T' or char=='V' or char=='W' or char=='X' or char=='Y' or char=='Z':
        consonant=consonant+1    
    elif char=='0' or char=='1' or char=='2' or char=='3' or char=='4' or char=='5' or char=='6' or char=='7' or char=='8' or char=='9':
        digit=digit+1
    else:
        specialChar=specialChar+1 
print("Vowels: ",vowel)
print("consonants: ",consonant)
print("digits: ",digit)
print("specialChars: ",specialChar)

print("===========================================================")
# 2nd approach using inbuilt string functions
# Program to find number of vowels,consonants,numbers and special characters

string1=input("Enter a string with alphanumeric and special characters: ")
string2=string1.lower()       # to avoid checking capital letters

# initializing values to zero
vowels=0
consonants=0
numbers=0
specialchar=0

# looping over the index of the input string
for char in range(0,len(string2)): 
    if string2[char] in ('a','e','i','o','u'):
        vowels+=1
    elif (string2[char] >= 'a' and string2[char] <= 'z'):
        consonants+=1
    elif string2[char].isnumeric()==1:
        numbers+=1
    else:
        specialchar+=1

print(f"Vowels={vowels}")
print(f"Consonants={consonants}")
print(f"numbers={numbers}")
print(f"specialchar={specialchar}")

print("===========================================================")
# Assin 2: Remove all the occurecences of multiple values in a list.

testlist=[1,4,4,4,2,3,3,3,3,2,2,2,2,2,7,5,5,7]
newlist=list(set(testlist))
print(newlist)
print("===========================================================")
#Program to generate random characters 
import string
import random

def UpperString(length):
    for x in range(length):
        result= random.choice(string.ascii_uppercase)
        print(result,end="")
def LowerString(length):
    for x in range(length):
        result1= random.choice(string.ascii_lowercase)
        print(result1,end="")
def MixedString(length):
    for x in range(length):
        result2= random.choice(string.ascii_letters)
        print(result2,end="")
def digits(length):
    for x in range(length):
        result3= random.choice(string.digits)
        print(result3,end="")
def punct(length):
    for x in range(length):
        result4= random.choice(string.punctuation)
        print(result4,end="")
def randomString(length):
    for x in range(length):
        result5= random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation)
        print(result5,end="")

UpperString(10)
print("")
LowerString(10)
print("")
MixedString(10)
print("")
digits(10)
print("")
punct(10)
print("")
randomString(10)


""" 
OUTPUT

JJOTFODIDE
vypjsskalm
tjAqOXUVWN
7891989586
>?,&!@;*."
/#,Tr:a=J) 

"""
print("====================================================================")
# To Import modules when full path is given.
import sys
sys.path.append('/Users/Nikhil-Nikhil-PC/DOCS/PYTHONMAY2021/main_module')

# the main_module directory contains module1.py, module2.py & moodule3.py
# module module1.py contains functions let's say getname
# module module2.py contains functions let's say encoding
# module module3.py contains functions let's say sum,mean,max,min

from module1 import getname
from module2 import encoding
from module3 import sum,mean,max,min