myset = {'pineapple', 'orange', 'apple', 'mango', 'banana', 'papaya', 8888, 'kiwi', 'cherry'}

myset.remove(8888)

print(myset)

myset.discard("banana")

print(myset)

x = myset.pop()
print(x)
print(myset)