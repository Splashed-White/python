# =======================列表的格式=========================
'''
    列表可以⼀次性存储多个数据，且可以为不同数据类型
'''

# =======================查找操作=========================
name_list = ['Tom','Lily','Rose']
print(name_list[0])  # Tom
print(name_list[1])  # Lily
print(name_list[2])  # Rose

 # index()：返回指定数据所在位置的下标
name_list = ['Tom','Lily','Rose']
print(name_list.index('Lily'))  # 1
#print(name_list.index('John'))  # 'John' is not in list

# count()：统计指定数据在当前列表中出现的次数
name_list = ['Tom','Lily','Rose']
print(name_list.count('Lily'))  # 1

# len()：列表中数据的个数
name_list = ['Tom','Lily','Rose']
print(len(name_list))  # 3

# in :判断指定数据在某个列表序列，如果在返回True，否则返回False
name_list = ['Tom','Lily','Rose']
print('Lily' in name_list)  # True

# not in：判断指定数据不在某个列表序列，如果不在返回True，否则返回False
name_list = ['Tom', 'Lily', 'Rose']
print('Lily' not in name_list)  # False

# =======================增加操作========================
# append():列表结尾追加数据
# 列表追加数据的时候，直接在原列表⾥⾯追加了指定数据，即修改了原列表
name_list = ['Tom', 'Lily', 'Rose']
name_list.append('John')
print(name_list)  # ['Tom', 'Lily', 'Rose', 'John']
print(name_list.append('John')) #None

# 如果append()追加的数据是⼀个序列，则追加整个序列到列表
name_list = ['Tom', 'Lily', 'Rose']
name_list.append(['xiaoming', 'xiaohong'])
print(name_list)  # ['Tom', 'Lily', 'Rose', ['xiaoming', 'xiaohong']]

# extend()：列表结尾追加数据，如果数据是⼀个序列，则将这个序列的数据逐⼀添加到列表
name_list = ['Tom', 'Lily', 'Rose']
name_list.extend('xiaoming')
print(name_list) # ['Tom', 'Lily', 'Rose', 'x', 'i', 'a', 'o', 'm', 'i', 'n', 'g']

# insert()：指定位置新增数据
name_list = ['Tom', 'Lily', 'Rose']
name_list.insert(1,'John')
print(name_list)  # ['Tom', 'John', 'Lily', 'Rose']

# =======================删除操作========================
# del 删除指定数据
name_list = ['Tom', 'Lily', 'Rose']
del name_list[0]
print(name_list)  # ['Lily', 'Rose']

# pop()：删除指定下标的数据(默认为最后一个)，并返回该数据
name_list = ['Tom', 'Lily', 'Rose']
name_list.pop(2)
print(name_list)  # ['Tom', 'Lily']

# remove():移除列表中某个数据的第⼀个匹配项
name_list = ['Tom', 'Lily', 'Rose']
name_list.remove('Rose')
print(name_list)  # ['Tom', 'Lily']

# clear()：清空列表
name_list = ['Tom', 'Lily', 'Rose']
name_list.clear()
print(name_list)  # []

# =======================修改操作========================
# 修改指定位置的数据
name_list = ['Tom', 'Lily', 'Rose']
name_list[0] = 'John'
print(name_list)  #['John', 'Lily', 'Rose']

# reverse():逆置
name_list = ['Tom', 'Lily', 'Rose']
name_list.reverse()
print(name_list)  # ['Rose', 'Lily', 'Tom']

# sort()：排序;reverse = True 降序， reverse = False 升序（默认）
num_list = [1,3,7,2,9,4]
num_list.sort()
print(num_list)  # [1, 2, 3, 4, 7, 9]

# =======================复制操作========================
# copy()：复制
name_list1 = ['Tom', 'Lily', 'Rose']
name_list2 = name_list1.copy()
print(name_list2)  # ['Tom', 'Lily', 'Rose']

# =======================列表的循环遍历========================
# while
name_list = ['Tom', 'Lily', 'Rose']
i = 0
while i < len(name_list):
    print(name_list[i])
    i += 1

# for
name_list = ['Tom', 'Lily', 'Rose']
for i in name_list:
    print(i)

# =======================列表嵌套========================
name_list = [['⼩明', '⼩红', '⼩绿'], ['Tom', 'Lily', 'Rose'], ['张三', '李四',
'王五']]
print(name_list[2][1])  # 李四  类似多维数组












