# 复制文件，小文件复制将file1中的内容复制到file2中

file1 = open('text1.txt', 'r')
file2 = open('text2.txt', 'w')

text = file1.read()
file2.write(text)


file1.close()
file2.close()
