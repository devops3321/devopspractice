row = int(input("Enter number of rows: "))
for row in range(row,0,-1): # Outer loop to iterate through rows
    for col in range(0,row): # Inner loop to iterate through columns
        print(row,end="")  
    print("")

# Enter number of rows: 5
# 55555
# 4444 
# 333  
# 22   
# 1