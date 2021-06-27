rows = int(input("Enter the number of rows: "))
for i in range(0,rows):  # iterating variable "i" should be different from rows (input)
    for k in range(0,rows-i): 
        print(" ",end="")
    for j in range(0,i+1):
        print("* ",end="")
    print("")

# Pattern

#      *   
#     * *  
#    * * * 
#   * * * *
#  * * * * *