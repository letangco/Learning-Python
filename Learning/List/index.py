thislist = list(('apple', 'banana', 'tomato'))
print(thislist[1])
print(thislist[-1])
print(thislist[1: 3])

if 'apple' in thislist:
    print("Yes, 'apple is exist'")
else:
    print("No, not exist")

thislist.insert(2, 'watermelon')
print(thislist)