# c. Variable length Args - v v imp. *vargs --> stored the args as a tuple.

def displayStudentNames(*names):
    print(names) # ('Aftab', 'Satya', 'Vijay', 'Nikhil') -> tuple.
    
''' displayStudentNames('Aftab')
displayStudentNames('Satya')
displayStudentNames('Vijay')
displayStudentNames('Nikhil') '''

displayStudentNames('Aftab','Satya','Vijay','Nikhil','Ankit',56)


# keyword length arguments -- **kwargs.
#x=5 # var=value - keyword

def person(**personData):
    print(personData) # {'name': 'John', 'age': 45, 'sal': 500.025} ---> Dictionary (k:v)
    print(personData.keys()) # dict_keys(['name', 'age', 'sal'])
    print(personData['age'])
    
person(name ='John', age =45, sal = 500.025)


# * - tuple
# ** - dictionary

