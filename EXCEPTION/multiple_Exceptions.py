


try:
    listx = [1,2,3,4,5]
    print(listx[90])
    
except Exception as e:

    print("Exception is raised,", e)
    
finally:
    print("always executed")
    


try:
    
    #sta 1
    #sta 2
    
    
    
    #sta15
    pass
except:
    #sta16
    #sta 17
    try:
        pass
    except:
        pass 

finally:
    #sta17
    pass