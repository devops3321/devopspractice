# rows = int(input("Enter the number of rows:"))  
# k = 2 * rows - 2  # It is used for number of spaces  
# for i in range(0, rows):  
#     for j in range(0, k):  
#         print(end=" ")  
#     k = k - 2   # decrement k value after each iteration  
#     for j in range(0, i + 1):  
#         print("* ", end="")  # printing star  
#     print("")  

# Pattern

#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * *

rows = int(input("Enter the number of rows: "))
for i in range(0,rows):
    for k in range(rows-i,0,-1):
        print(" ",end="")
    for j in range(0,i+1):
        print("* ",end="")
    print("")