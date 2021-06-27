'''
function parameters - types
a. Positional Arguments/params or required args/params - Values MUST be passed.
b. Default Args/params
c. Variable Lenght Args - v v imp.
d. Keyword Length Args - m imp concept.

'''

# a. Poistional
def add(x,y,z):
    print(x+y+z)
    
add(2,4,9)

#b. Default args
def add(x,y,z=10):
    print(x+y+z)
    
add(1,2,8)

# error, 11, 

def add(x,y=5,z=10):
    print(x+y+z)
    
add(1,2,3)
'''
    def add(x,y=10,z):
            ^
SyntaxError: non-default argument follows default argument
'''



# area of cube = l*b*h
# breadth is always fixed to 10

def areaOfCube(l,h,b=10):
    area = l*b*h
    print(area)
     
areaOfCube(1,2)


