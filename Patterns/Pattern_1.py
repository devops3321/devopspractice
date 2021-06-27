# Pattern 1
row = int(input("Enter the number of rows: "))                                  
num=1
for row in range(0,row+1):
    for col in range(0,row):
        print("",num,end="")
        num+=1
    print("")

#  1
#  2 3
#  4 5 6
#  7 8 9 10
#  11 12 13 14 15