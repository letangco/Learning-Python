fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

print('-------------------------------------------------------')

for x in fruits:
    print(x)

newlist = [x.upper() for x in fruits if 'a' in x]
print(newlist)

print('----------------------------------------------------')

j = 0
while j < len(fruits):
    if 'e' in fruits[j]:
        print(fruits[j]) 
    j = j +1