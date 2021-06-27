row = int(input("Enter number of rows: "))
for row in range(0,row+1): # Outer loop to iterate through rows
    for col in range(0,row): # Inner loop to iterate through columns
        print("*",end="")  
    print("")

# pattern

# *    
# **   
# ***  
# **** 
# *****