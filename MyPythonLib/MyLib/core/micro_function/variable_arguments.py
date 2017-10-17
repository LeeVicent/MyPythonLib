#################################
'''
#功能：变参函数，实现任意数量的列表相加
#参数：*args  参数包，可以使用for语句迭代展开参数
'''
def arry_add(*args):
    li = []
    for x in args:   #args为元组
        li += list(x)
    return li

##################################
'''
#解压序列给多个变量
'''

name, num, tup = ['jianghe', 202140721, (12, 10)]  #参数数量匹配即可直接解压
print(name, num, tup)
                                                                                  #注意元组，列表之类的书写方式
name, num, (x, y) = ['jianghe', 202140721, (12, 10)]  #若内部包含数据结构，可再次解压（依然需要参数匹配）
print(name, num, x, y)

x, y, z = 'heh'  #解压字符串，所有可迭代对象都能解压
print(x, y, z)

#如果只需要部分，则用占位符（任意）代替之，到时扔掉即可
_, num, _ = ['jianghe', 202140721, (12, 10)] 

#*表达式解压出任意数量参数
first, *middle, last = (1, 2, 3, 4)    #*表达式可放在任意位置，总是获取剩余元素
print(middle)      #middle = [2, 3]  解压不定长度参数时为列表，和变参函数不一样（变参为元组）

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
] 

#不同于 JavaScript 这样的动态语言，Python 函数调用前必须定义
def do_foo(x, y):
    print('foo', x, y)
def do_bar(s):
    print('bar', s)

for tag, *args in records:    #for 迭代的过程即可解压，这点很重要
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)