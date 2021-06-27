# add country='USA'
def allDataParam(name,*lang,country='USA',**books):
    print(name,lang,books,country) # John ('English', 'Spanish', 'Deuth') {'book1': 'author', 'book2': 'author2'}
    

allDataParam('John','English','Spanish','Deutsch','Hindi',country='INDIA', book1='author1', book2 = 'author2', book3 = 'author3')

