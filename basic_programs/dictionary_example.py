myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print('My cat has ' + myCat['color'] + ' fur.')

spam = {12345: 'Luggage combination', 42: 'The Answer'}

print([1, 2, 3] == [3, 2, 1])

eggs = {'name': 'Zophie', 'species': 'cat', 'age':8}
ham = {'species': 'cat', 'name': 'Zophie', 'age': 8}
print(eggs == ham)

print('name' in eggs)

print(list(eggs.keys()))
print(list(eggs.values()))
print(list(eggs.items()))

# Print keys in dictionary
for k in eggs.keys():
    print(k)

print()

# Print values in dictionary

for v in eggs.values():
    print(v)

print()

# Print tuples in dictionary

for i in eggs.items():
    print(i)

print()

# Print key and value separated by a single space

for k, v in eggs.items():
    print(k,v)

print()

# Check if cat is a value in dictionary

print('cat' in eggs.values())

''' Provide default value if key not found in dictionary with
    get method to dictionary'''


print(eggs.get('age', 0))
print(eggs.get('color', ''))


picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('napkins',0)) + ' napkins to the picnic')

# Set default key value if not present in dictionary

bacon = {'name': 'Sam', 'species': 'cat', 'age':7}
bacon.setdefault('color', 'black')
print(bacon)

# Does not change value of default key if key is already present in dictionary
bacon.setdefault('color', 'orange')
print(bacon)
