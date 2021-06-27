try:
    print(a)
except NameError as msg:
    print(msg)
    print(type(msg))
    
    print(msg.__class__)
    print(msg.__class__.__name__)
    