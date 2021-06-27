# eval()
age = 45
print(eval('age+15')) # TypeError: eval() arg 1 must be a string, bytes or code object

b1=bytes('hello', encoding='utf-8') # b'hello'
print(b1)

b=bytes(10)
print(eval('b'))

print(eval('dir()'))
print(eval('bytes()'))


''' name ='hello'
print(eval('name+1')) '''



print(pow(2,4,5)) # 2pow3=8 anmd then 8/2, remainder =0

print(divmod(4,2)) # (2, 0)


from math import *

print(dir())

# sqrt()
print(sqrt(9))


cal = { 'sq_root': sqrt, 'power':pow}
print(cal['sq_root'])
print(eval('sq_root(16)',cal)) # sq_root(16) --> sqrt --->16
print(eval('power(2,3)',cal))


print(pow(pow(2,3),2)) 

import math
print(math.sqrt(9))
print(math.tan(45))


# convert the str into integer without the int function and vice versa 
x=3
print(type(eval('x')))

''' intValue= input("Enter age  ")

print(type(intValue)) '''


print("===========")
evaleg = eval(input("enter random stuff     "))
print(type(evaleg))








