""" for i in range(1,100):
    print(i) """
    
import random 
# random value between 0.0 - 1.0 
print(random.random()) # 16 digits after the . 
print(random.randint(35,708))

listx=[1,2,3,4,5,1,6,7,5,'ankit','satya'] # set is called a map-sequence based object.
print(random.choice(listx))

#listx = [] # empty list, does not mean its a list with 0 as element.
#print(random.choice(listx)) # IndexError: Cannot choose from an empty sequence
# None, 0, error 

print("=====")
#random.randint(listx[0], listx[11]) 
listx1 = [1,2,'two']
print(random.choices(listx1,weights=[1,1,10],k=3))


numbers = [2,4,6,8,10,12,14] 
print("before shuffle, ", numbers)
random.shuffle(numbers) # - always operates on the original list.
print("after")
print(numbers)

# seed
#print(random.seed(4))
numbersPrime = [1,2,3,5,7,11]
print(random.random())

# seed - it will save the state of random function - and will not change it with every re-run of random()
# generate a "random" number ONCE and then preserve it. This is also called preserving the "state" of random()

print("======")
for i in range(5):
    random.seed(0)
    print(random.randint(1,10))
    #print(random.random())

# assign - generate a random passwrd usiong the random module.


