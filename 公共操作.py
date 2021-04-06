# ==============  +  ======================
# 1. 字符串
str1 = 'aa'
str2 = 'bb'
str3 = str1 + str2
print(str3) # aabb
# 2. 列表
list1 = [1, 2]
list2 = [10, 20]
list3 = list1 + list2
print(list3) # [1, 2, 10, 20]
# 3. 元组
t1 = (1, 2)
t2 = (10, 20)
t3 = t1 + t2
print(t3) # (1, 2, 10, 20)

# ==============  *  ======================
# 1. 字符串
print('-' * 10) # ----------
# 2. 列表
list1 = ['hello']
print(list1 * 4) # ['hello', 'hello', 'hello', 'hello']
# 3. 元组
t1 = ('world',)
print(t1 * 4) # ('world', 'world', 'world', 'world')

# ==============  in / not in  ======================
# 1. 字符串
print('a' in 'abcd') # True
print('a' not in 'abcd') # False
# 2. 列表
list1 = ['a', 'b', 'c', 'd']
print('a' in list1) # True
print('a' not in list1) # False
# 3. 元组
t1 = ('a', 'b', 'c', 'd')
print('aa' in t1) # False
print('aa' not in t1) # True

# ==============  公共方法  ======================
# len()
# 1. 字符串
str1 = 'abcdefg'
print(len(str1)) # 7
# 2. 列表
list1 = [10, 20, 30, 40]
print(len(list1)) # 4
# 3. 元组
t1 = (10, 20, 30, 40, 50)
print(len(t1)) # 5
# 4. 集合
s1 = {10, 20, 30}
print(len(s1)) # 3
# 5. 字典
dict1 = {'name': 'Rose', 'age': 18}
print(len(dict1)) # 2

# del()
# 1. 字符串
# str1 = 'abcdefg'
# del str1
# print(str1)  # error
# 2. 列表
list1 = [10, 20, 30, 40]
del(list1[0])
print(list1) # [20, 30, 40]

# max()
# 1. 字符串
str1 = 'abcdegf'
print(max(str1)) # g
# 2. 列表
list1 = [10, 20, 40, 30]
print(max(list1)) # 40

# min()
# 1. 字符串
str1 = 'abcdefg'
print(min(str1)) # a
# 2. 列表
list1 = [10, 20, 30, 40]
print(min(list1)) # 10

# range():range()⽣成的序列不包含end数字
# 1 2 3 4 5 6 7 8 9
for i in range(1, 10, 1):
    print(i)
# 1 3 5 7 9
for i in range(1, 10, 2):
    print(i)
# 0 1 2 3 4 5 6 7 8 9
for i in range(10):
    print(i)

# enumerate()
list1 = ['a', 'b', 'c', 'd', 'e']
for i in enumerate(list1):
    print(i)
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')
# start参数⽤来设置遍历数据的下标的起始值，默认为0
for index, char in enumerate(list1, start=1):
    print(f'下标是{index}, 对应的字符是{char}')
# 下标是1, 对应的字符是a
# 下标是2, 对应的字符是b
# 下标是3, 对应的字符是c
# 下标是4, 对应的字符是d
# 下标是5, 对应的字符是e

# ==============  容器类型转换  ======================
# tuple()：将某个序列转换成元组
list1 = [10, 20, 30, 40, 50, 20]
s1 = {100, 200, 300, 400, 500}
print(tuple(list1))
print(tuple(s1))

# list()：将某个序列转换成列表
t1 = ('a', 'b', 'c', 'd', 'e')
s1 = {100, 200, 300, 400, 500}
print(list(t1))
print(list(s1))

# set()：将某个序列转换成集合
list1 = [10, 20, 30, 40, 50, 20]
t1 = ('a', 'b', 'c', 'd', 'e')
print(set(list1))
print(set(t1))

# ==============  列表生成式  ======================
# 创建一个0-10的列表
# 法1：while
list1 = []
i = 0
while(i < 10):
    list1.append(i)
    i += 1
print(list1)

# 法2：for
list1 = []
for i in range(10):
    list1.append(i)
print(list1)

# 法3：列表生成式
list1 = [i for i in range(10)]
print(list1)

# 创建一个0-10的偶数列表
# 法1：range步长实现
list1 = [i for i in range(0,10,2)]
print(list1)

# 法2：if实现
list1 = [i for i in range(10)  if i % 2 == 0]
print(list1)



















