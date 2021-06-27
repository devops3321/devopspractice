
# else in exceptions - only in PY

try:
    pass 
except: #expression as identifier:
    pass 
else:
    pass 


# else - will ONLY run if there is no exception.

try:
    a=3
    result=a/0
    print(result)
except: 
    print("Execution is thrown")
else:
    result +=3
    print(result)
    print("else code")
    
#finally - expection thrown or not thrown - it will always be executed
finally:
    print("finally block")
    


'''
exception thrown - and u dont want to execute another piece of code then else block.
exception thrown or not thrown but you want the code to excecute at all costs - finally block.


'''
    
    
try:
    pass
    try:
        pass
    except:
        pass
    finally:
        pass
except:
    pass 
    try:
        pass
    except:
        pass
    finally:
        pass
finally:
    pass


'''
Rules
try and execept is possible
try and finally is possible

try and else - not possible - as else is always after the except.
try, except and else - is possible.

try, else, finally - will NOT work
"else" - "except" go hand in hand.

'''

try:
    print('try')
    
except:
    print('in except')
   
else:
    print('Ankit') 
    
finally:
    if 20<30:
        print("true")
    else:
        print("False")
        
# open connection
# DML operatons
# add, delete
# print(f)
# finally:
# close connection.



    



