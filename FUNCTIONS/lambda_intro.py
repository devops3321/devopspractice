# lambda - unknown, anonymous - there is no function name
# A lambda func can take any number of arguments, BUT CAN only  have ONE expression.

# no def keyword - named function.
# syntax

# lambda parameter_list : expression

addTwo = lambda x:x+2
print(addTwo(2))

#print(lambda y:y+3) # <function <lambda> at 0x020B8DA8>

addxy = lambda x,y:x+y
print(addxy(3.5,4.8))

def addtwo(x,y):
    result = x +y
    print(result)

addtwo(1,2)

'''
map()
reduce()
filter()
'''

print ("===*vargs====")
#areaofcube = l*b*h
areaOfCube=lambda l,b,*h:l*b*h
print(areaOfCube(2,2,2)) # (2, 2, 2, 2)

# *h-> (2,)
# 4((2,)) 
print(4 * (2,))
# error,8, empty tuple



print ("======kwargs=")

''' areaOfobject=lambda l,b,*h,**z:l+b+h+z
print(areaOfobject(1,2,3,a=2,x=2))

t=2
d = {'a':2,'b':5}

print(t*d) '''

'''
Assign: Try addiont on dict in this lambda eg
once you figure out how to do that or if its not possible
then try to use the keys in the lambda funciton

'''

# Assign2:
sumSub = lambda u,v: (u+v,u-v)
print(sumSub(4,2))

# lambda function cannot take more than one expression at a time.
# but it can take n no of args.

# jump to functionScope.py