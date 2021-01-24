set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1.update(set2)

print(set1)

print('--------------------------------------')
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
# Return về phần tử trùng của 2 sets
x.intersection_update(y)
print(x)
# Return về phần tử trùng nhưng được gán giá trị mới
z = x.intersection(y)
print(z)

print('----------------------------------------')
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}

c = a.symmetric_difference(b)
print(c)
# Trả về set item không trùng của 2 set
a.symmetric_difference_update(b)
print(a)

