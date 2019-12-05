def eggs(cheese):
    cheese.append('Hello')

spam = list(range(1,4)) # spam = [1, 2, 3]
eggs(spam)
print(spam)

# Deep copy list

import copy
ham = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(ham)

cheese[1] = 42

print('ham:\t',end = '')
print(ham)
print('cheese:\t',end = '')
print(cheese)
