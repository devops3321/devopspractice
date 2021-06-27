# with open(<filepath>, <mode>) as <nameofvar>

with open("Filesex1\withdemo.txt", 'w') as withdemotxt:
    withdemotxt.write('this is a demo for "with" keyword \n')
    withdemotxt.writelines("This is the second line")   

print(withdemotxt.closed)



 

