# =====================字符串形式=============================
name = 'Tome'
name = '''Tome,
        Nice to meet you''' # 三引号字符串可以换行

# =====================字符串输出=============================
name = 'Tom'
print(f'我的名字是{name}')
print('我的名字是%s'%name)

# =====================字符串输入=============================
password = input('请输入密码')
print(f'用户的密码是：{password}')

# =====================字符串下标=============================
num = 'abcde'
print(num[0])
print(num[4])

# =====================字符串切片=============================
'''
    序列[开始位置下标：结束位置下标：步长]
    1.从起始位置开始，到结束位置的前一位数据
    2.步长可正可负，默认为1
    3.步长代表每隔几位取一个元素
'''
num = 'hello world'
print(num[6:10:2]) # wr
print(num[1:10:2]) # el ol
print(num[1:10:3]) # eoo
print(num[1:]) # ello world
print(num[::2]) # hlowrd
print(num[:-1]) # hello worl  负1表示倒数第⼀个数据
print(num[::-1]) # dlrow olleh

# =======================字符串查找============================
# 字符串查找：查找子串在字符串中出现的位置或出现的次数
'''
    1.find():检测某个⼦串是否包含在这个字符串中，如果在返回这个⼦串开始的位置下标，否则则返回-1
        字符串序列.find(⼦串, 开始位置下标, 结束位置下标)
'''

mystr = 'hello world and itcast and itheima and Python'
print(mystr.find('and')) # 12
print(mystr.find('and',15,30))  # 23
print(mystr.find('ands')) # -1

'''
    2.index():检测某个⼦串是否包含在这个字符串中，如果在返回这个⼦串开始的位置下标，否则则报异常
        字符串序列.index(⼦串, 开始位置下标, 结束位置下标)
'''

mystr = 'hello world and itcast and itheima and Python'
print(mystr.index('and')) # 12
print(mystr.index('and', 15, 30)) # 23
print(mystr.index('ands')) # 报错

'''
    3.rfind():和find()功能相同，但查找⽅向为右侧开始
    4.rindex():和index()功能相同，但查找⽅向为右侧开始
'''
'''
    5.count():返回某个⼦串在字符串中出现的次数
        字符串序列.count(⼦串, 开始位置下标, 结束位置下标)
'''
mystr = 'hello world and itcast and itheima and Python'
print(mystr.count('and')) # 3
print(mystr.count('ands')) # 0
print(mystr.count('and', 0, 20)) # 1

# =======================字符串修改=========================
# 字符串修改：通过函数的形式修改字符串中的数据
'''
    1.replace():替换
        字符串序列.replace(旧⼦串, 新⼦串, 替换次数)
'''

mystr = 'hello world and itcast and itheima and Python'
print(mystr.replace('and','111'))
# 结果：hello world he itcast he itheima he Python
print(mystr.replace('and', 'he', 10))
# 结果：hello world and itcast and itheima and Python

'''
    2.split():按照指定字符分割字符串
        字符串序列.split(分割字符, num)
        num表示分割字符出现的次数，从左到右数如果达到了次数，即使还有分割字符也不再进行分割
        分割后会丢失分割字符
'''
mystr = 'hello world and itcast and itheima and Python'
print(mystr.split('and'))
# ['hello world ', ' itcast ', ' itheima ', ' Python']
print(mystr.split('and',2))
# ['hello world ', ' itcast ', ' itheima and Python']

'''
    3.join():⽤⼀个字符或⼦串合并字符串，即是将多个字符串合并为⼀个新的字符串
        字符或⼦串.join(多字符串组成的序列)
'''
list1 = ['chuan', 'zhi', 'bo', 'ke']
print('_'.join(list1)) # aa...b...cc...ddd
t1 = ('aa', 'b', 'cc', 'ddd')
print('...'.join(t1)) # chuan_zhi_bo_ke

# 4.capitalize():将字第一个字符换成大写
str = 'hello world'
print(str.capitalize()) # Hello world

# 5.title():将字符串中每个单词的首字母转换成大写
str = 'hello world'
print(str.title()) # Hello World

# 6.lower()：将字符串中⼤写转⼩写
str = 'Hello World'
print(str.lower()) # hello world

# 7.upper()：将字符串中⼩写转⼤写
str = 'hello world'
print(str.title()) # Hello World

# 8.lstrip()：删除字符串左侧空⽩字符
str = ' hello world'
print(str.lstrip()) # hello world

# 9.strip()：删除字符串右侧空⽩字符
str = 'hello world  '
print(str.rstrip()) # hello world

# 10.strip()：删除字符串两侧空⽩字符
str = ' hello world  '
print(str.strip()) # hello word

# 11.ljust():返回⼀个原字符串左对⻬,并使⽤指定字符(默认空格)填充⾄对应⻓度 的新字符串
# 12.rjust():返回⼀个原字符串右对⻬,并使⽤指定字符(默认空格)填充⾄对应⻓度 的新字符串
# 13.center():返回⼀个原字符串居中对⻬,并使⽤指定字符(默认空格)填充⾄对应⻓度 的新字符串

# =======================字符串判断==========================
# 判断返回的结果是布尔类型的True或False
'''
    1.startswith():检查字符串是否是以指定⼦串开头，是则返回 True，否则返回 False。如果设置开始和结束位置下标，则在指定范围内检查。
        字符串序列.startswith(⼦串, 开始位置下标, 结束位置下标)
'''
str1 = 'hello world'
print(str1.startswith('hello',5,10))

'''
    2.endswith()：：检查字符串是否是以指定⼦串结尾，是则返回 True，否则返回 False。如果设置开始和结束位置下标，则在指定范围内检查。
        字符串序列.endswith(⼦串, 开始位置下标, 结束位置下标)
'''
str2 = 'hello world'
print(str2.endswith('ld'))

'''
    3.isalpha()：如果字符串⾄少有⼀个字符并且所有字符都是字⺟则返回 True, 否则返回 False
'''
mystr1 = 'hello'
mystr2 = 'hello12345'
print(mystr1.isalpha()) # True
print(mystr2.isalpha()) # False

'''
    4.isdigit()：如果字符串只包含数字则返回 True 否则返回 False。
'''
mystr3 = 'aaa12345'
mystr4 = '12345'
# 结果： False
print(mystr3.isdigit())
# 结果：False
print(mystr4.isdigit())

'''
    5.isalnum()：如果字符串⾄少有⼀个字符并且所有字符都是字⺟或数字则返 回 True,否则返回False
'''
mystr5 = 'aaa12345'
mystr6 = '12345-'
print(mystr5.isalnum()) # True
print(mystr6.isalnum()) # False

'''
    6.isspace()：如果字符串中只包含空⽩，则返回 True，否则返回 False
'''
mystr7 = '1 2 3 4 5'
mystr8 = ' '
print(mystr7.isspace()) # False
print(mystr8.isspace()) # True










