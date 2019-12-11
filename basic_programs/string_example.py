spam = """hello wolrd hellow orld good by ed lsdl two"""
print(len(spam))

spam2 = "hello world!"
print("Is it all lower-cased? " + str(spam2.islower()))
spam3 = spam2.upper()
print("Is it all upper-cased? " + str(spam3.isupper()))
print(spam3.lower().isupper())
print(spam3.lower().islower())


spam4 = 'hello'
print(spam4.isalpha())

spam5 = 'hello 123'
print(spam5.isalpha())
print(spam5.isalnum())

spam6 = '12345'
print(spam6.isdecimal())

spam7 = '           '
print(spam7.isspace())
print(spam5[5].isspace())

spam8 = 'this is not title case'
print(spam8.title().istitle())

spam9 = 'Hello Beaver!'
print(spam9[1:5].startswith('ello'))
print(spam9[3:5].endswith('o'))

joinStrings = ','.join(['cats', 'rats', 'bats'])
print(joinStrings)

spam10 = 'My name is Simon'
print(spam10.split())
print(spam10.split('m'))

print('Hello'.rjust(10))
print('Hello'.ljust(10))
print('Hello'.rjust(20,'*'))
print('Hello'.center(20, '='))

spam11 = 'Hello'.rjust(10)
print(spam11.strip())

spam12 = 'BOB'.center(30,'=')
print(spam12.lstrip('='))
print(spam12.rstrip('='))

spam13 = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam13.strip('ampS'))

spam14 = spam13.replace('Spam', 'Dodo')
print(spam14)

import pyperclip
pyperclip.copy('hello!!!!!!!!!!!!')
print(pyperclip.paste())
