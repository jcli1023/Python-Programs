name = 'Zophie a cat'

newName = name[0:7] + 'the' + name[8:]

print('name: ' + name)

print('newName: ' + newName)

# Show immutability of str in python
try:
    name[1] = 'a'
except TypeError:
    print('Strings in python are immutable, cannot change at an index.')
    print('TypeError caught by attempting name[1] = \'a\'')
