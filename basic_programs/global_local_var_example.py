spam = 42 # global variable

def eggs():
    spam = 43 # local variable
    print('local spam: ' + str(spam))

print ('global spam: ' + str(spam))
eggs()
