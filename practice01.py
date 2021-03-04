#  确定不同整型数据类型在内存中占多大（字节），输出不同整型数据类型在内存中占多大（字节）

print("The size of short is 2 bytes.")
print("The size of int is 4 bytes.")
print("The size of long is 8 bytes.")
print("The size of long long is 8 bytes.")

#  十进制整数1234对应的八进制和十六进制（字母大写），用空格分开，并且要求，在八进制前显示前导0，在十六进制数前显示前导0X

print("0%o 0X%X" % (1234,1234))

# C        printf("%d",10);
# python   print("%d" % 10)

#  十六进制整数ABCDEF对应的十进制整数，所占域宽为15

print("%15d"%(0XABCDEF))

# %md   控制输出m位的域宽

#  输出：
#  第一行为“Hello world!”
#  第二行为printf(“Hello world!”)调用后的返回值

a = "Hello world!"
print(a)
print(len(a))
#len() 返回字符串中的字符数，列表中的项目数