# file level is global
x=5 # scope is global or global var 

def sumeg(x,y):
    print("x inside the function - ", x)
    print(x+y) # x and y is local var or in other words the scope of x is local to this funciton called sumeg()

sumeg(4,5)

#print(y) # NameError: name 'y' is not defined
x=10

print("x outside the function - ", x)

# 9, 10, error.


print("======")

a=12 

def sumeg1(a,b):
    a=a+10
    print("a inside the function - ", a)
    print(a+b) 

sumeg1(a,5) # -----> sumeg1(12,5)
print("a outside of function", a)
# error, 17 
