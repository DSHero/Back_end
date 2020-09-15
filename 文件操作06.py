# 大文件复制，通过单行复制

file1 = open('text1.txt', 'r')
file2 = open('text2.txt', 'w')

while True:
    text = file1.readline()
    if not text:
        break
    file2.write(text)

file1.close()
file2.close()
