import os


# Viết file (a -> append vào)
f = open('./fileDoc.txt', 'a')

f.write("\nNow the file has more content!")
f.close()
# Đọc file
f = open('./fileDoc.txt', 'r')
print(f.read())
f.close()

print('-----------------------------------')
# Tạo mới file
# newFile = open('product.txt', 'w')

print('-------------------------------')
# Delete file

if os.path.exists('./product.txt'):
    os.remove("product.txt")
else:
    print('The file does not exist')


if os.path.exists('./foldertest'):
    os.rmdir('foldertest')
    print('Delete folder success')
else: print('The folder does not exist')

