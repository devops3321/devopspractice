import os 
print(os.name)

print(os.getcwd())

try: 
    os.mkdir('satyadir')
except (FileExistsError,FileNotFoundError) as fe:
    print("Error is - ", fe)

finally:
    os.rmdir('satyadir')
    
# os.close()
file_obj = open ("file1.txt", 'w') 
file_obj.write("Hello this is a python script")
#os.close(file_obj)
file_obj.close()
if file_obj.closed:
    print("file is closed")
else:
    print("file is still open for editing please close it at the end")
    
#file_obj.write("This is after close") # - this line will result into error as the file is closed.

print(os.getcwd())
print("====")
os.chdir('../../..')
print(os.getcwd())

# "\" 
os.chdir('/Users')
print(os.getcwd())

os.chdir('/Users/trade/Python_May2021')
#os.rename('files12.txt', 'file1123.txt')

print(os.cpu_count())

