# ===================元组的定义=========================
# 1. ⼀个元组可以存储多个数据，元组内的数据是不能修改的
# 2. 定义元组使⽤⼩括号，且逗号隔开各个数据，数据可以是不同的数据类型
# 3. 如果定义的元组只有⼀个数据，那么这个数据后⾯也好添加逗号，否则数据类型为唯⼀的这个数据的数据类型

# 多个数据元组
t1 = (10, 20, 30)
# 单个数据元组
t2 = (10,)
print(type(t2))  # tuple

t3 = (20)
print(type(t3)) # int

# ===================元组的查找操作========================
tuple1 = ('aa', 'bb', 'cc', 'bb')
print(tuple1[0])  # aa

# index()：查找某个数据，如果数据存在返回对应的下标，否则报错
tuple1 = ('aa', 'bb', 'cc', 'bb')
print(tuple1.index('aa')) # 0

# count()：统计某个数据在当前元组出现的次数
tuple1 = ('aa', 'bb', 'cc', 'bb')
print(tuple1.count('bb')) # 2

# len()：统计元组中数据的个数
tuple1 = ('aa', 'bb', 'cc', 'bb')
print(len(tuple1)) # 4

# 元组内的数据不能修改
# tuple1 = ('aa', 'bb', 'cc', 'bb')
# tuple1[0] = 'aaa'  # error















