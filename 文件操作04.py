# readline()：读取一行，用于大文件


file = open('text1.txt')

while True:
    text = file.readline()
    # 判断是否读取内容
    if not text:
        break

    print(text)


file.close()
