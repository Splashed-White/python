# =================字典的定义============================
# 字典⾥⾯的数据是以键值对形式出现，字典数据和数据顺序没有关系，即字典不⽀持下标，
# 后期⽆论数据如何变化，只需要按照对应的键的名字查找数据即可

# 有数据字典
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'} # key:value
# 空字典
dict2 = {}
dict3 = dict()

# =================字典的增操作============================
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
dict1['name'] = 'Rose'
print(dict1)  # {'name': 'Rose', 'age': 20, 'gender': '男'}

dict1['id'] = 110
print(dict1)  # {'name': 'Rose', 'age': 20, 'gender': '男', 'id': 110}

# =================字典的删操作============================
# del() / del：删除字典或删除字典中指定键值对
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
del dict1['gender']
print(dict1)  # {'name': 'Tom', 'age': 20}

 # clear()：清空字典
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
dict1.clear()
print(dict1)  # {}

# =================字典的改操作============================
# 如果key存在则修改这个key对应的值 ；如果key不存在则新增此键值对; 同定义例子

# =================字典的查操作============================
# key查找:如果当前查找的key存在，则返回对应的值；否则则报错
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1['name']) # Tom
# print(dict1['id']) # error

# get():如果当前查找的key不存在则返回第⼆个参数(默认值)，如果省略第⼆个参数，则返回None
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1.get('name'))
print(dict1.get('id', 110)) # 110
print(dict1.get('id')) # None

# keys()
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1.keys()) # dict_keys(['name', 'age', 'gender'])

# values()
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1.values()) # dict_values(['Tom', 20, '男'])

# items()
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
print(dict1.items()) # dict_items([('name', 'Tom'), ('age', 20), ('gender','男')])

# =================字典的循环遍历============================
# 遍历key
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
for key in dict1.keys():
    print(key)
# name
# age
# gender

# 遍历value
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
for value in dict1.values():
    print(value)
# Tom
# 20
# 男

# 遍历字典的元素
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
for item in dict1.items():
    print(item)
# ('name', 'Tom')
# ('age', 20)
# ('gender', '男')

# 遍历键值对
dict1 = {'name': 'Tom', 'age': 20, 'gender': '男'}
for key, value in dict1.items():
    print(f'{key} = {value}')
# name = Tom
# age = 20
# gender = 男






