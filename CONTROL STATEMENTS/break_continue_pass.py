''' for letter in 'Satya':
    print(letter)
    break '''

cars = ['Audi', 'Merc', 'RR', 'BMW']

for car in cars:
    if car == 'RR':
        break
    print(car)
print("Line no 11")    

fruits = ['orange','banana','grapes']

for x in fruits:

    if x == 'banana':
        pass
        print('I am after pass')
        
print(x)
        
print("line no 21")

#pass - just continue without error - skip and continue what you were doing.
for x in [1,2,3,4]:
    pass


#continue - current iteration of loop will be stopped, and "continue" to the next statement in the loop.
fruits = ['orange','banana','grapes']

for x in fruits:

    if x == 'banana':
        pass
        print("I am after continue")
    print(x)
    
# Orange, IAM,banana, grapes.

for x in range(2,8,2): # 2,4,6
    print(x)
    

