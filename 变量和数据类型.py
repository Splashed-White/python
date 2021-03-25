
# =============================数据类型================================
a = 1
print(type(a)) # <class 'int'> -- 整型
b = 1.1
print(type(b)) # <class 'float'> -- 浮点型
c = True
print(type(c)) # <class 'bool'> -- 布尔型
d = '12345'
print(type(d)) # <class 'str'> -- 字符串
e = [10, 20, 30]
print(type(e)) # <class 'list'> -- 列表
f = (10, 20, 30)
print(type(f)) # <class 'tuple'> -- 元组
h = {10, 20, 30}
print(type(h)) # <class 'set'> -- 集合
g = {'name': 'TOM', 'age': 20}
print(type(g)) # <class 'dict'> -- 字典

# =============================格式化输出================================
print('我的名字是%s'%'Tom') # 我的名字是Tom
print('f我的名字是{Tom}') # 我的名字是Tom
print('hello',end = '...')
print('world') # hello...world

# =============================输入================================
'''
    当程序执行到input 时，会等待用户的输入，输入完成之后才继续执行
    无论接收到什么数据，都当作字符串处理
'''
password = input('请输入密码:')
print(f'用户的密码为:{password}')
print(type(password)) # <class 'str'>




















