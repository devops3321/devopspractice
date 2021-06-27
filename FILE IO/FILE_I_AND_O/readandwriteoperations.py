try:
    file=open('Filesex1/Juneeg3.txt','r+')
    if file.readable:
        output=file.readlines() 
        print(output)
    if file.writable:
        file.write("hello this is third time month")
    if file.closed == False:
        file.close()
except Exception as e:
    print("Exception is -, ", e)
    
    #\n - new line character.