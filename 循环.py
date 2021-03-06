# ===================== while ====================================
i = 0 # 计数器
while i < 5:
    print('while循环举例')
    i += 1
print('任务结束')

# ===================== while实例：1-100累加 =========================
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(f'累加结果为：{sum}')

# ===================== while实例：1-100偶数累加 =========================
# 法1：模2
i = 1
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum += i
    i += 1
print(f'累加结果为：{sum}')

# 法2：计数器
i = 0
sum = 0
while i <= 100:
    sum += i
    i += 2
print(f'累加结果为：{sum}')

# ===================== break ================================
'''
    break：终止此循环
    continue:退出当前一次循环而执行下一次循环的代码
'''
i = 1
while i < 5:
    if i == 4:
        print(f'吃饱了不吃了')
        break
    print(f'吃了第{i}个苹果')
    i += 1

# ===================== continue ==========================大虫子，第{}
i = 1
while i <= 5:
    if i == 3:
        print(f'大虫子，第{i}个不吃了')
        i += 1
        continue
    print(f'吃了第{i}个苹果')
    i += 1

# ===================== while循环嵌套:打印星号 =========================
# 重复打印5星星
j = 0
while j < 4:
    # 一行星星的打印
    i = 0
    while i < 4:
        print('*',end = '') # 一行内的星星不能换行，取消print默认结束结束符\n
        i += 1
    print() # 每行结束利用空的print()换行
    j += 1
'''
    ****
    ****
    ****
    ****
'''

# ===================== while循环嵌套:打印星号 =========================
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print('*',end = '')
        j += 1
    print()
    i += 1
'''
    *
    **
    ***
    ****
    *****
'''

# ===================== while循环嵌套:九九乘法表 =======================
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f'{j}*{i}={i*j}',end = '\t')
        j += 1
    print()
    i += 1

# ===================== for循环 =======================
str = 'hello'
for i in str:
    if i== 'l':
        print('遇到l不打印')
        break
    print(i)

# ===================== while else =======================
'''
    while 条件:
        条件成立重复执行的代码
    else:
        循环正常结束后执行的代码
'''
i = 1
while i < 5:
    print('循环执行')
    i += 1
else:
    print('任务结束')

# ===================== for else =======================
'''
    for 临时变量 in 序列:
        重复执行的代码
    else:
        循环正常结束后执行的代码
'''
str = 'hello'
for i in str:
    print(i)
else:
    print('任务结束')


