
inputstr = 'november'
# out = ['n','o,'v'....]
emptylist = []
for letter in inputstr:
    emptylist.append(letter)

print(emptylist)

print("====list comprehension approach=======")
''' output = [letter for letter in inputstr]
print(output) '''
print([letter for letter in inputstr])
# [var1 for item in sequenceobj (not just list)]
# [[var1,var2 .....varn] for item in sequenceobj (not just list)]

#PS - range(1,101) - print only even numbers in a list of range.
print([x for x in range(1,101) if x%2==0])

print([i for i in range(1,15) if i%2==0 
       for j in range(8) if j%2==0])


print("=========")
''' output= [(x1,x2) for x1 in range(1,15) if x1%2==0 else print('else')
         for x2 in range(5) if x2%2!=0] '''
         
newstyle = ['even' if x%2==0 else 'odd' for x in range(6)] # -> 0,1,2,3,4,5
print(newstyle)

'''
psuedo-code to explain above

m='even'
n='odd'
for a in range(6):
if a%2==0:
    append(m)
else:
    append(n)
'''

print("===============tuples=============")
# to create generators one way is to use tuple comprehension.
tupleVal = (x for x in range(5))
print(tupleVal) # <generator object <genexpr> at 0x01D8E9C8>
