stuff = {'name' : 'Z' ,'age' : 39 , 'height': 6 * 12 + 100}

print (stuff['name'])
print(stuff['age'])
print(stuff['height'])

stuff['city'] = "SF"
print(stuff['city'])

stuff[1] = "wow"
stuff[2] = "Neato"

print(stuff[1])
print(stuff[2])

print(stuff)

del stuff['city']
del stuff[1]
del stuff[2]

print(stuff)
