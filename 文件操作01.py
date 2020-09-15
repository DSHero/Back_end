# 文件操作三大步骤:
#     1.打开文件
#     2.读、写文件
#         读 将文件内容读入内存
#         写 将内存内容写入文件
#     3.关闭文件

# open:打开文件
# read:将文件内容读取到内存
# write:将指定内容写入文件
# close:关闭文件


# 打开文件
file = open('text1.txt')

# 读取文件
text = file.read()
print(text)

# 关闭文件
file.close()
