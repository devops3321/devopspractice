name ='Ankit' # 0- A, 1-n, 2-k, 3-i, 4-t
print(name.endswith('a'))

text = 'Najam is good'
print(text.find('good'))

# count() - for a part word AND case sensitive.

print(name.count('t'))

news = 'This is an example of a title'
print(news.title()) #This Is An Example Of A Title

firstName = 'Ankit'
lastName = "Pahwa"

#print(name.join('Pahwa')) #PAnkitaAnkithAnkitwAnkita

# concatenation of strings.
print(firstName + ' ' + lastName) #Ankit Pahwa
firstVariable=2
secondVariable=4
print(firstVariable + secondVariable )


# name.casefold("") 
# Ankit   
print(name.upper()) #ANKIT
print(name.lower()) #ankit

# check the strings
name='ANKIT'
print(name.islower())
print(name.isupper())
print("ankit".islower())
print(name.isdecimal()) # possible usecase

#spilt()
print(name.split('K')) #an, it.--> ['AN', 'IT']

# index()
greeting = 'Good Morning, its a nice morning'
print(greeting.index('Morning')) # 5 - # m char position or index
print(greeting.index('m')) # 25

# find()
text = 'Najam is good, Good guy'
#print("=====")
#print(text[0:5]) #Najam
print(text.find('good'))
print(greeting.find("Morning"))  # 5

print("====find and index diff====")
# find() vs index()
print(greeting.find("good")) # -1 (depicts error)
print(text.index('M')) # error. - ValueError: substring not found


if text.index('najam') == -1:
    print("It does not exist")
else:
    print("it exists")


    




