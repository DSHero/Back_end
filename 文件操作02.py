# 文件指针
# 通常指打开文件读取内容，文件指针默认移动到文件末尾，
# 再次读取并不会读取到文件内容.



file = open('text1.txt')

text = file.read()
print(text)
print(len(text))

print('-' * 50)

text = file.read()
print(text)
print(len(text))

file.close()
