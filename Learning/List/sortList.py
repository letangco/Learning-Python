thislist = [100, 50, 65, 82, 23]
thislist_char = ['cherry', 'tomato', 'banana', 'apple', 'watermelon']
thislist.sort()
print(thislist)

thislist_char.sort(reverse = True)
print(thislist_char)

print('-------------------------------------------')

def my_Function(n):
    return abs(n - 50)

thislist.sort(key = my_Function)
print(thislist)
print('-------------------------------------------')
# Đảo ngược chiều danh sách
thislist.reverse()
print(thislist)
# Copy sẽ tạo tham chiếu đến thislist làm thay đổi danh sách

newList = thislist
print('newList: ', newList)
newList.pop()

newList2 = thislist.copy()

print('newList2: ', newList2)