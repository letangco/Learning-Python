thislist = ['apple', 'banana', 'cherry', 'watermelon', 'tomato']

for x in thislist:
    print(x)
print('-------------------------------------------')
for i in range(len(thislist)):
    print(thislist[i])

print('-------------------------------------------')
j = 0
while j <len(thislist):
    if j % 2 == 0:
         print(thislist[j])
    j = j + 1
print('-------------------------------------------')

[print(x) for x in thislist]

print('-------------------------------------------')

newlist = [x.upper() for x in thislist if 'a' in x]
print(newlist)