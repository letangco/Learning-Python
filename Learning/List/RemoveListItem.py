thislist = ['apple', 'banana', 'watermelon']
# Delete item in list
thislist.remove('apple')
thislist.remove(thislist[0])

# delete first item in list
thislist.pop()
del thislist[0]
# delete all item in list
thislist.clear()

print(thislist)