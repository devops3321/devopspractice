# can else work in an loop

for x in [1,2,3,4,5]:
    
    if x == 3:
        break
    print(x)
else:
    print("finally finished")
    
print("After for else")