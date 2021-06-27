# indexing

text = 'baseball'
''' print(text[2]) # s

name ='ankit'
print(name[2]) #k '''

print(text[7]) #8 will be error - IndexError: string index out of range

print(text[-5]) # e 

print(text[-8])

print("=====")
str1 ='Najam'
'''print(str1[-2]) #a
print(str1[1:1]) # a, nothing. '''

# slicing
# [start index : stop index(-1): step value]
print(str1[1:4:1])  # aja

name ='Aftabkhan'
print(name[2:9:1]) # tabkhan
print(name[2:9:2]) # tbhn
print(name[2:9:3]) # tkn

print(name[2::])  # tabkhan -> [2:9:1]
print(name[:5:])  # Aftab-> [0:5:1]
# [start index : stop index(-1): step value]
print(name[::3])  # Aah -> [0:9:3]

newtext= 'Good Morning its a beatufil day'

print(newtext[::]) 

text1= ' Ganesh'
print(text1[:6:2]) # GNS correct is  <space>ae

# strings - are immutable
name = 'Hello'
print(name)
name[4] = 'w' # 0 -> w # TypeError: 'str' object does not support item assignment
print(name) # Hellw