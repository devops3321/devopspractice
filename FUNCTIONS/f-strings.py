# 3.6
# f-string. f 'string'
sport = 'baseball'
print(f'I like a sport, and the sport is  {sport}')

score = 7.89
print(f'my score is {score}')

print(f'{2*4}')

print(f'{True == False}') # False

def to_uppercase(string1):
    return string1.upper()

greetings = "hello, good morning"
print(f'{to_uppercase(greetings)}')

name ='Ankit'
messages = (
    f'hi {name}',
    f'hello {name}' ,
    f'hey {name}',
)

print(messages)

rice =4.53789
milk = 2.6789

print(f'rice is {rice:.2f}')

print(type(f'')) # <class 'str'>


