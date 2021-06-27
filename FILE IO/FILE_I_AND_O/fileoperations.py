fileObj = open('Filesex1/Sample.txt', 'r+')
#properties

print(fileObj.name)
print(fileObj.readable())
print(fileObj.writable())
fileObj.close()
print(fileObj.closed)