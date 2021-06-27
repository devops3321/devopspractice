# with while it will execute " as long as the condition is true"
# in for we execute until the conditon becomes false.

# while expression:
#   block of code

count =0
while count < 4:
    print(count)
    count = count +1
 

# 0,1,2,3

print("Satya's")
listx = [1,2,3,4,5,6,7,2,9,3]

count = 0
while listx[count] < 4:
    print(listx[count])
    count=count+1

listy = [1,2,3,4,5,6,7,2,9,3]
count1=0
print("nikhils")
while count1 < len(listy):
    if listy[count1] < 4:
        print(listy[count1])
    count1 = count1 +1
    
print ("++++++++++++++++")    
i =1
while i <6:
    print(i)
    if i ==3 :
        break
    i+=1 #(i=i+1)

    
# 4,///1,2/// 1,2,3 //

#while-else

print("====while-else=====")

i =1
while i <6:
    print(i)
    i+=1 #(i=i+1)
else: 
    print('i is no longer less than 6')
