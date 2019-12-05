supplies = ['pens', 'staplers', 'binders'] * 4

# Iterate through a list using len(list) for any list size
for i in range(len(supplies)):
	print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# Multiple assignment
cat = ['fat', 'orange', 'loud']

size, color, disposition = cat

size, color, disposition = 'skinny', 'black', 'quiet'
