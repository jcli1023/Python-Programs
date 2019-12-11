name = 'Alice'
place = 'Main Street'
time = '6 pm'
food = 'turnips'
sentence = 'Hello ' + name + ', you are invited to a party at ' + place + ' at ' + time + '. Please bring ' + food + '.'
sentenceFormat = 'Hello %s, you are invited to a party at %s at %s. Please bring %s.' % (name, place, time, food)

print(sentence)
print(sentenceFormat)
print(sentence == sentenceFormat)
