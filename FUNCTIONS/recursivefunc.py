# Recursive function - a functuion that calls itself. - v tricky and int fav.

def recursiveFunc(i):
    if (i > 0):
        result =  i + recursiveFunc(i-1) # res = 3 +recfu(2) -> res =3+3 -----> return 6
        # recfu(2) -> res = 2 + recfu(1) -> 1, res = 2+1=3. ------> retrun 3
        # recfu(1) - > res = 1 + recfu(0) -> 1+ 0, --------> return 1
        # recfu(0) ------> return 0
        print(result)
    else:
        result =0
        
    return result 

print("\n\n Recursive Example output")
recursiveFunc(3)


