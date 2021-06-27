# nested if - if within an if 

x =18

if x > 10:
    print("X is above 10")
    if x > 20:
        print("X is also above 20")
    else:
        print("but is less than 20 - else of inside if")
else :
    print("Else of outer if")
    
    

if [1,2,3] == [1,2,3.0]: # set do not follow indexing, its just checking the values.
    print (True)
else:
    print(False)

setex= {1,2,3.0}
print(setex)



