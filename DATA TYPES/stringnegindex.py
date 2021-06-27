# [start index : stop index (-1): step value]
name ='Mohan'
print(name[-1:-6:-2]) #nhM

print(name[::-1]) # nahoM

# how do u check for a palindrome string
# palindrome string is a string which is same as its orig string in the reverse direction also
# eg ABBA, MOM

text ='MALAYALAM'
print(text[::]) #+1
print(text[::-1]) #MOM

print("===Mohan===")
print(name[::])
print(name[::-1]) #reverses the string

print(text[::] == text[::-1])  # == check a condition 
print(name[::] == name[::-1]) # False
''' 
a=5
b=10
print(a==b) '''

print("=====Abhilash output=====")
# [start index : stop index (-1): step value]
name1 = 'Abhilash'
print(name1[-1:-4]) # hi, hlb, hsa, error, emptry is the ans
print(name1[-1:-4:-1]) # hsa

print(name1[-3:-7:-1]) #alih

print("===Question ====")
print(name1[9]) # 0:9
