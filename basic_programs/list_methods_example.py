# List methods work in place and not return a new list

spam = ['cat', 'dog', 'bat']
spam.append('moose')

spam.insert(1, 'chicken')

for i in range(len(spam)):
    print(str(i) + '. ' + spam[i])

print()

spam2 = ['cat', 'bat', 'rat', 'elephant', 'hat', 'cat']
spam2.remove('cat')

for i in range(len(spam)):
    print(str(i) + '. ' + spam[i])

print()


# Sort in descending order
spam2 = [2, 5, 3.14, 1, -7]
spam2.sort(reverse = True)
print(spam2)


spam3 = ['Alice', 'Bob', 'ants', 'badgers', 'Carol', 'cats']

# Sort in ASCII-betal order
spam3.sort()
print(spam3)

# Sort in true alphabetical order
spam3.sort(key = str.lower)
print(spam3)
