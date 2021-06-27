
colors = ['blue', 'yelow','red']
objects = ['water', 'mangoe', 'cherries']

for x in colors:
    for y in objects:
        print(x,y)
    print("outisde inner for loop and within outside for loop")    

print("outside all loops")

print("======")
'''
1
22
333
4444
'''

for i in range(1,4): # 1,2,3
    for j in range(0,i):
        print(i, end ='****')
    print()
        
print("-----end eg ------")        
# end keyword
x = 'ankit'
y = 'pahwa'

print(x, end=" ")
print(y)

