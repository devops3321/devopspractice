dict6 ={
'brand' : 'audi',
'model' : 'q5', #modell
'year' : 2021,

}

listValues=[]
for values in dict6.values():
    listValues.append(values)
print(listValues) ## printig the values of the dict dict6
print('=====================================')

print("using for loop to change the key")
listKeys= []

for key in dict6.keys():
    listKeys.append(key)

listKeys[1] = 'modell'
print(listKeys)
print('=====================================')
finalDict={}
i=0
for i in range(0,3):
    finalDict[listKeys[i]]=listValues[i]

dict6=finalDict ## Overriding the dict dict6
print(dict6)


dict7 ={
'brand' : 'audi',
'model' : 'q5', #modell
'year' : 2021,

}

finalDict2 ={
'brand' : 'audi',
'modell' : 'q5', #modell
'year' : 2021, 
}

dict7=finalDict2
print(dict7)


dict6 = {'brand': 'audi', 'model':'q5', 'year':2021}
print("The original Dictionary is :", dict6)
dict6['modell'] = dict6['model'] # -->modell : q5
print("after updating")
print(dict6)
del dict6['model']
print("after del")
print("The new updated dictionary is:", dict6)



dict1 = {'one':1, 'two':2, 'three':3}
dict2 = {'four':4, 'five':5}

dictx=[]
for i in dict1,dict2:
    dictx.append(i)
    print(dictx)
final = {}
final['end']=dictx
print(final)
print(type(final))

#Nikhils
empnew={}
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


#satyas
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


for ankit,nikhil in dict2.items():  
    #print(key,value)
    dict3[ankit]=nikhil   ### adding the keys and values of dict2 into dict3 - appending at the end.

print("printing below the concatenation of dictionaries dict1 and dict2")
print(dict3)  ### printing the concatenated value of dict1 and dict2



str1='vijaykumar'
print(str1[-1:5:-1])

# # Using  nested if, else
num = float(input("Enter a number: "))
if num >=0:
    if num == 0:
        print("Zero")
    else:
        print("Positive Number")
else:
    print("Negetive number") 

# =========================================

# Using if, elif and else

num = float(input("Enter a number: "))
if num >0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negetive number")

# ===============================
sum = 0
for iterVar in range(1,101):
    sum = sum + iterVar
print(sum)

# ==========================

num = int(input("Enter a number: "))
count =0
for count in range(1,11):
    product = num * count
    print(num,"x",count, "=", product)

# ================================
# function to create average marks.
def average_marks(marks):
    sum_of_marks=sum(marks)
    total_subjects=len(marks)
    average_marks=sum_of_marks/total_subjects
    return average_marks

def grade(average_marks):
    if average_marks>=80:
        print("Your grade is A")
    elif average_marks>=60:
        print("Your grade is B")
    elif average_marks>=50:
        print("Your grade is C")       
    else:
        print("Your grade is F")
        return grade  

marks=[45,66,77,71,84]
print("The average marks is: ",average_marks)

print("The average marks is: ",grade)

print("=================================")

def factorial(x):
    if x==1:
        print(x)
        return 1
    else:
        return(x*factorial(x-1))
num=3
print("The factorial of",num, "is", factorial(num))

print("=================================")
def largestEven(list_num):
    curr=-1
    for num in list_num:
        num=int(num)
        if (num%2==0 and num>curr):
            curr=num
    return curr
        
def largestOdd(list_num):
    currO=-1
    for num in list_num:
        num =int(num)
        if (num%2==1 and num>currO):
            currO=num
    return currO
        

list_num=[1,3,5,8,6,10]
print("Largest even number is ", largestEven(list_num))
print("Largest Odd number is ", largestOdd(list_num))
print("=================================")


