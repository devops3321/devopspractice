# format() and print formatting - pre 3.5 Python version
# {} - placeholder.....curl braces
newstr = 'hello, {}'.format('Aftab')
print(newstr)

newstr1 = 'hello, {}; Your score is {}'.format('Ankit',86)
print(newstr1)

name = 'John'
noOfProjects = 47
#print("Name of the employee is ", name, '& No of project he is working on - ', noOfProjects)


# %d - int, %s - string, %f - float

print("Name of the employee is " +name+ ' & No of project he is working on are', noOfProjects)

message2 = "Name of the employee is {} & No of project he is working on are {}".format(name,noOfProjects)
print(message2)

exam1 = 78.894978787
examscore = 78.894973787
avgScore = "Exam average score {0} ....is .....{1:.5f}".format(exam1,examscore)
print(avgScore)


milkprice= 123.89754321615898968
print("Milk Price of today is rounded to the fourth place is {0:.4f} ".format(milkprice))


numx = [9.5,6.7890,0.345]
strlist = 'List formatting {0}..... '.format(numx,numx)
print(strlist)

# print formatting
name = 'Python'
print('hello , %s' %name)

person_name="john"
person_age = 45

print("Person Details, Person name is %s, and person age is %s" %(person_name,person_age))

rice = 4.53
milk = 2.56

print("rice quantity is %.1f and milk quantity is %s" %(rice,milk))








