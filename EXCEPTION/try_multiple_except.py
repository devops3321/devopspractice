try :
    print(a) # NameError
    x=5
    result = x/1 # zeroDivison Error
    
#except (NameError,ZeroDivisionError) as e:
except NameError as e:
    print("Exception is raised",e)


print("outside except")

# alias - as 


    
    