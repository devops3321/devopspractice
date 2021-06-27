file = open('Filesex1\seektellnotexist.txt', 'r')
#file.write("This is June month, and year is 2021")
print(file.tell())
#file.seek(-6,2) # seek will take -ve and/or +ve integer values.
print(file.read()) 

#print(file.seekable()) # even an empty file is seekable.
file.close()

print(file.seekable())


'''
0 - start of the file
1 - current position
2 - eof

'''



