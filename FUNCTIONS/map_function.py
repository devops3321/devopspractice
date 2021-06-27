# map , filter, reduce
listex = [1,2,3,4,5]
print("===Firstway====")   
newlist = []
for i in listex:
    i=i**2 # ** - squaring of the number * means multiplication.
    newlist.append(i)
print(newlist) 

# map() - takes 2 args. first is function itself and second is a sequence.
# map(function,sequence)
print("===Secondway====")   
def squareValues(n):
    return n**2 
print(list(map(squareValues,listex)))

''' output= map(squareValues,listex)
print(output) # <map object at 0x0239AB50>
print(list(output))  '''

 

''' output2 = map(lambda n : n**2, listex)

print(list(output2)) '''

''' output3 = lambda n: n**2
output3(listex) # ---> output3([1,2,3,4,5])
print(list(output3)) '''

print("===Thirdway====")
print(tuple(map(lambda n : n**2, listex)))


numbers = [1,2,3,4,5,6,7,8,9,10]

print("====Firstway of filter=====")
#PS - find even numbers and then square those

newlist = []
for i in numbers:
    if i%2 == 0: # if a number is even or not
        newlist.append(i**2)
print(newlist)

print("====Secondway of filter=====")

def evenNumbers(n):
    if n%2==0:
        return n**2

""" outputFilter = filter(evenNumbers,numbers)
print(list(outputFilter)) """
# print(list(map(evenNumbers,numbers))) # [None, 4, None, 16, None, 36, None, 64, None, 100]

print(list(filter(evenNumbers,numbers)))

print("====Thirdway of filter=====")
print(list(filter(lambda n:((n%2==0)*(n%2==0)),numbers)))


# reduce() 
#print(reduce())
listx= [1,2,3,4,5]
listsum = sum(listx)
print(listsum)

j=0
for i in listx:
    j=j+i
print(j)

""" l =lambda listx : sum(listx)
print(l) """


from functools import reduce
#print(reduce())

print(reduce(lambda x,y:x+y,listx[2:]))

# map - works on all or apply on all elements
# filter - works on conditions and filters only "SOME"
# reduce - reduce it to one value eg sum, avg, mode,mean, median. - it doesnt return the memory address.


