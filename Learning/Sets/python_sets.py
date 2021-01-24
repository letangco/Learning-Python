# KHông có thứ tự xác định
# không cho phép các giá trị trùng lặp
# Không thể được tham chiếu
myset = {"apple", "banana", "cherry", "cherry"}

print(myset, type(myset))

myset1 = set(("apple", "banana", "cherry"))
print(myset1)

print('---------------------------------------')
for x in myset:
    print(x)