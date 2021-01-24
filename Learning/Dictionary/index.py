thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print(thisdict['model'])

print(len(thisdict))

print(type(thisdict))

arrKeys = thisdict.keys()
arrValues = thisdict.values()
arrItem = thisdict.items()

print(arrKeys)
print(arrValues)
print(arrItem)

thisdict['car'] = 'Audi'
thisdict['year'] = 2021
print(thisdict)


thisdict.pop('car')

del thisdict['year']
print(thisdict)


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(car.get("model"))
print(car['model'])