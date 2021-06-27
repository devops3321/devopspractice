row = int(input("Enter the number of rows: "))
for row in range(row,0,-1):
    for col in range(0,row):
        print("*",end="")
    print("")

# Pattern
# *****
# ****
# ***
# **
# *
