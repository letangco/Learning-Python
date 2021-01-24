list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2

print(list3)

print('-----------------------------------------------------')

for x in list2:
    if x % 2 == 0:
        list1.append(x)

print(list1)
print('-----------------------------------------------------')

list2.extend(list1)
print(list2)