row = int(input("Enter number of rows: "))
for row in range(1,row+1): # Outer loop to iterate through rows
    for col in range(1,row+1): # Inner loop to iterate through columns
        print(col,end="")  
    print("")

# print the following pattern
# 1
# 12
# 123
# 1234
# 12345
