#import os
#coding = utf-8 
#var1 = 10
#var2 = 20

#print(var1, var2)  #python3.5 不带两边的括号
#print(var1, var2, sep = "")  #sep指定位空串可以取消var1， var2的空格

#print("My name is {} ".format("Jiang", "He"))  
#print("My name is {} {}".format("Jiang", "He"))  

#print("{0:f}".format(2523.2))   #25.200000  不指定精度自动填充满
#print("{0:s}".format("Test"))
#print("{}".format("Test"))

#temp = ["Jiang", 12, "He"]   #类型可以不一致
#print(temp)   #运行结果：['Jiang', 12, 'He']

#nums = [5, 10, 4, 5]
#name = ['Jiang', 'He', 'he']

#print(name)

#以下运行结果都为['name', 'test']
#print("name**test".split('**'))   #以自定义字符串分隔
#print('name test'.split())     #以默认空格分隔
#print("name\ntest".split())  #以默认换行符分隔，感觉用在文件读写上挺好
#print("name\ttest".split())   #以默认制表符分隔

#name = ['Jiang', 'He']
#print(" ".join(name))  #结果Jiang He

#t = "a", "b", "c"   #一般不写括号
#t = ("a", "b", "c")  
#print(t)       #打印结果  ('a', 'b', 'c')
#t[1] = "s"   #TypeError    'tuple' object does not support item assignment

#x, y, z = 5, 6, 7       #创建x, y, z三个变量，并分别赋值5, 6, 7
#(x, y, z) = (5, 6, 7)   #其实上面就是创建匿名元组tuple(x, y, z)进行赋值
#x = 10         #合法，x, y, z虽然属于匿名元组，但是不是通过下标运算符修改
#                   相当于C++容器中通过元素名直接操作元素
#name, num = "Jianghe", 25   #创建匿名元组tuple("Jianghe", 25)

#使用元组交换两个变量的值
#x = 10    #匿名元组tuple(x)
#y = 20    #匿名元组tuple(y)
#x, y = y, x  #实质为tuple(20, 10)赋值给tuple(10, 20) 
#                 实现原理估计就是位运算，为元组对象重载 = 运算符

#jiang = [("jianghe", 5, 7),(56, 'hehe')]   #元组列表定义
#print(jiang[0][1])   #5

#目前已知的修改元组方式只有整体重新赋值
#t = 10, 20   #定义元组
#t = 20, 30
#t = t[0]
#print(t)

#L1 = [5, 6]
#L2 = L1   #浅拷贝，L2，L1指向同一块内存
#L2 = list(L1)  #深拷贝，L2指向list()函数创建的L1副本
#L2 = L1[:]     #深拷贝，引用切片副本

#t = 2,    #单元素元组末尾有逗号","
#print(t)

#print("ji" in "jianghe")   #True  #关键字in判断是否为子串
#print("ji" not in "jianghe")   #False  #关键字in判断是否为子串

#print([10, 20] > [10, 21])   #False  不同元素决定断言结果
#print([10, 20] > [10, "WTF"])   #Type Error   #unorderable types: int() > str()
#print([10, 20] > [10])    #True  比较长度

#print([10] in [10, 20])   #False  #in运算不能直接比较两个列表的包含关系
#print(10 in [10, 20])     #True   #in运算只能用于元素和列表的包含关系
#print(10 not in [10, 20])   #False、

#print("jianghe".startswith("ji"))
#help(chr)

#print(isinstance(10, int))
#print(isinstance("sa", str))
#print(isinstance([10], list))
      
#(state == "A") or (state == "B") or (state == "C") or (state == "D")    
#state in ["A", "B", "C", "D"]              #使用in简化单值的多次or运算        

#(x < 10) or (x > 20)   #传统写法
#10 < x < 20  #Python独有写法，连续逻辑判断以变量为中心拆成上述语句

#if 2 > 5:
#    a = 5
#    if 2 < 5:    #ifqi
#        x = 6
#    else:
#        x = 7
#else:
#    b = 2

#x = 20
#if x > 5:
#    x = 10
#elif x < 5:
#    x = 20
#else:
#    x = 20
#else:
#    x = 20

#a = 10;
#c = 20

#num1 = input("Please input your first name: ")
#num2 = input("Please input your second name: ")

#if num1.isalpha() and num2.isalpha():   #断言num1和num2全为字母
#    print("Your name is:", num1, num2)
#elif not num1.isalpha():      #断言num1不全为字母
#    if not num2.isalpha():     #断言num2不全为字母
#        print("Neither entry was a proper str.")
#    else:
#        print("The first entry was not a proper str.")
#else:
#    print("The second entry was not a proper str.")

#while 1 > 2:  #使用缩进代替括号
#    a = 10
#    break

#for var in sequence
#        indented block of statment


#for i in range(8):  #i不需要定义，for会遍历后面的容器并赋值给i
#    print(i)  #输出 0~7
         
#infile = open("1.txt", 'r')   #打开文件
#for x in infile:
#    print(x, end = "")   #按行输出文件内容
#infile.close()   #关闭文件

#for i in range(8):  #for循环仅用于遍历
#    pass  #执行空语句，不写的话报错


#print(list(range(2, 20, -4)))  #s < 0, 返回空序列
#print(list(range(200, 20, 4)))   #m >= n, 返回空序列
#num = 20

#a = 200

#temp = 6   #temp位模块层全局变量
#def f():
#    global temp  #声明全局变量temp
#    temp = 20    #修改全局temp，而不是定义局部temp


#num = 0
#while num < 10:
#    num = num + 1 #迭代
#    if num >15:
#        break   #num > 15 时跳出循环
#else:
#    print("num没有小于15")

#days = ['Monday', 'Tuesday', 'Wednesday']
#fruits = ['banana', 'orange', 'peach']
#drinks = ['coffee', 'tea', 'beer']
#desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
#for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
#    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)

#import module1   #导入模块“model1.py”

#num = 10   #定义模块层全局变量 num

#module1.display(num)   #使用 “模块名“ 调用 ”模块内函数“
#print(module1.gl)   #使用 “模块名“ 读取 ”模块内全局“
#module1.gl = 40   #修改module1全局变量（合法）

#def fun():
#    global module1.gl    #SyntaxError: invalid syntax
#    module1.gl = 20  #无需声明，可读取并且可以修改
#    print(module1.gl)
#    gl = 30  #定义局部变量，估计是命名空间的问题（合法）
#    print(gl) 

#fun()

#from module1 import *  #直接导入module所有内容

#print(gl)     #打印module1.gl(相当于全局)

#gl = 20   #修改module1.gl

#display(10)   #全局函数module.dispaly()

#def display(num):   #再次定义，覆盖module.dispaly()
#    print(num)
#    print(gl)     #打印module1.gl
#    gl = 30   #UnboundLocalError:  local variable 'gl' referenced before assignment

#display(20)    #内层定义覆盖

#def fun():
#    num1 = 10
#    num2 = 20
#    return num1, num2    #返回元组(num1, num2)
#   或者这样写return (num1, num2)

#fun()[0] = 2  #TypeError :'tuple' object does not support item assignment
#print(fun())    #打印(10, 20)

#def fun():  #重定义，覆盖之前的fun()
#    num1 = 10
#    num2 = 20
#    return [num1, num2]   

#print(fun())  #打印[10, 20]
#print(isinstance(fun(), list))  #True  断言成功



#print([x ** 2 for x in (1, 2, 3) if x <= 2])

#等价于
#noName = []  #定义一个空列表
#for x in (1, 2, 3):
#    if x <= 2:
#        noName.append(x ** 2)   #if断言为真，则尾插入之
#print(noName)

#def fun(x, num = 2):
#      pass

#def fun(x, y, z):
#    print(z)

#fun(10,  20, y = 30)   #TypeError--形参表中未关键字传参的参数在y的右边
#fun(10, 20, z= 30)   #合法

#temp = [9, 20]
#lambda temp : temp

#def fun():   #定义fun()函数
#    print("ds")

#def f(fun):   #定义f()函数，形参为fun函数名
#    fun()       #函数f内部调用fun()

#f(fun)    #调用f(fun)函数
#stairs = ['thud', 'meow', 'thud', 'hiss']

#def edit_story(words, func):
#    for word in words:
#        print(func(word))

#          lambda只用于函数调用时，当做一个匿名函数传递进去
#edit_story(stairs, lambda word: word.capitalize() + '!')    #lambda作用是在str后加一个“！”


#st = "dsad"

#def fun(x, y, c, z = 10):
#    pass
#fun(10,c = 20)  #关键字参数未满
#                        TypeError：fun() missing 1 required positional argument: 'y'
#a = ["ds"]
#infile = open("1.txt", 'r')   #打开文件


#li = [x.rstrip() for x in infile]
#print(li)  
#infile.close()   #关闭文件

#print("dsad\t".rstrip())
#print("dsad   ")


#infile = open("1.txt", 'r')   

#s = " "   #定义一个str
#while s != "":
#    s = infile.readline()   #readline每遍历一行，就返回一次str
#    print(s.strip(), end = "")   #删除各行换行符，并关闭print自动换行

#infile.close()   

#def file_copy(infile_str, outfile_str):
#    infile = open(infile_str, 'r')
#    outfile = open(outfile_str, 'w')

#    outfile.writelines([x for x in infile])   #行写入
#    infile.close()
#    outfile.close()

#file_copy("1.txt", "3.txt")


#自带换行写入
#def file_append_str(file_name, append_str):
#    if os.path.isfile(file_name):
#        infile = open(file_name, 'a')  #不清空文件，尾插入
#        infile.write(append_str + "\n")
#        print("str \""+ append_str + "\" append success!")
#        infile.close
#    else:
#        print(file_name + "doesn't exit!")
    
#file_append_str("3.txt", "test")


#se = {10}

#se.add(20)

#print(se.add(20))


#以list of list方式返回CSV文件内容    #二维数组
#def file_CSV_read_list(file_name):
#    if os.path.isfile(file_name):
#        fin = open(file_name)                  
#                             先对record移除末尾的'\n'，在拆分成list of str
#        temp_lsit = [x.rstrip().split(',') for x in fin]   #temp_list is an list of str(field)
#        return temp_lsit
#    else:
#        print(file_name + "doesn't exit!")


#li = file_CSV_read_list("3.txt")
#print(li)

#te = { "dsa1":"sda", 123:45}

#print(isinstance(te.keys()))
#for x in te.keys():
#    print(x)

#t = dict([5, 6])

#te[123] = 50

#print(t)

#print(te.items())
#print(list(te.items()))



#import pickle

#temp_dict = { "dsa1":"sda", 123:45}

#fout = open("5.txt", 'wb')   #fout对象仅能执行写操作相关函数
#pickle.dump(temp_dict, fout)   #以二进制写入，记事本打开乱码
#fout.close()

#fin = open("5.txt", 'rb')  #fin对象仅能执行读操作相关函数
#temp_dict = pickle.load(fin)
#print(temp_dict)
#fin.close()

#dic = {x:x + 1 for x in [1,2,3,4]}
#print(isinstance(dic, dict))

#class MyClass:   
 
#    def __init__(self, value = 20):     
#        self.__value = value   #双前导下划线
    
#    @property    
#    def value(self):    
#        print("get_value() function has been called")
#        return self.__value


#    @value.setter  
#    def value(self, value):
#        print("set_value() function has been called")
#        self.__value = value   


#s = MyClass(10)     
#s.value     #合法
#s.value = 30     #合法
#print(s._MyClass__value)



#s._a = 20
#s._temp = 30
##print(s._ds)
#print(s.get_a())
#print(s.get_value())
#print(s.get_temp())
#print(s._temp)       #所有成员支持类外访问，Python没有访问权限控制

#class sun(MyClass):
#    def __init__(self, value = 20, new = 30):
#        super().__init__(value)   #调用父类构造方法初始化
#        self._new = new  #新增成员变量

#    def get_value(self):      #重写，隐藏父类get_value()方法
#        return self._new       #暂时不知道如何调用父类隐藏方法

#su = sun(10, 20)
#print(su.get_value())


#ds = MyClass()

#print(ds)

#def fun():
#    print("dsa")

#def fun(x = 10):
#    print("123")
#fun(20)




#class A():
#    count = 0    #定义类级变量，即static

#    def __init__(self):
#        A.count += 1     #构造方法中修改类级变量count

#    def exclaim(self):     #exclaim  v.  呼喊
#        print("I'm an A!")

#    @classmethod       #类级方法声明
#    def kids(cls):         #第一个参数为cls
#        print("A has", cls.count, "little objects.")    #cls.cout == A.cout

#    @staticmethod
#    def display():
#        print("hehe")

#object1 = A()   
#object1 = A()
#object1  = A()
#A.kids()
#A.display()


#class little_MM:
#    def girl_says(self):
#        print("I Love You")

#    def result(self):
#        print("Success")

#class little_GG:      #little_GG hasn't any relationship with little_MM 
#    def boy_thinks(self):
#        print("hehe...")

#    def result(self):    #little_GG has a function  as same as little_MM's
#        print("Die")

#def display_result(obj):   #odj can bind to any object(dynamic binding)
#    obj.result()

#girl = little_MM()
#boy = little_GG()
#display_result(girl)   #Success
#display_result(boy)    #Die


#class B:
#    def __init__(self, b):
#        self._b = b

#    @property
#    def b(self):
#        return self._b
#                                 #class B提供比较规则，覆盖__eq__(应该是和Java一样有一个超类Object)
#    def __eq__(self, other_obj):   
#        return self.b.lower() == other_obj.b.lower()  #比较规则无关大小写

#    def __repr__(self):
#        return "dsada"

#b1 = B("jiang")
#b2 = B("JIANG")
#print(b1 == b2)    #True

#b1


#from collections import namedtuple   #导入特定内容
                                      
#Duck = namedtuple('Duck', 'bill tail')  
#print(isinstance(Duck, tuple))   
#parts = {'bill': 'wide orange', 'tail': 'long'}
#duck = Duck(**parts)
#print(isinstance(duck, tuple))     #True duck为命名元组，因为其为子类


#print(duck)
#print(duck.bill)   
#print(duck.tail)   



#class Bill():
#    def __init__(self, description):
#        self.description = description

#class Tail():
#    def __init__(self, length):
#        self.length = length

#class Duck():
#    def __init__(self, bill, tail):
#        self.bill = bill
#        self.tail = tail
#    def about(self):
#        print('This duck has a', bill.description, 'bill and a',
#        tail.length, 'tail')

#tail = Tail('long')
#bill = Bill('wide orange')
#duck = Duck(bill, tail)
#duck.about()

#from bs4 import BeautifulSoup
################################GUI###
#from tkinter import *   #Python自带GUI库 tkinter

#window = Tk()   #创建Tk类的实例名为window
#window.title("Test")   #设置窗体名
#btn = Button(window, text = "hehe", bg = "light blue")

#btn.grid(padx = 75, pady = 15)

#window.mainloop()  #mianloop()函数无限循环，监听事件，直至单击关闭按钮

#from urllib.request import urlopen   #导入urlopen函数
#from urllib.error import HTTPError
#from bs4 import BeautifulSoup    #导入BeautifulSoup类

#try:          #确保网页在服务器上存在
#    html = urlopen("http://www.pythonscraping.com/pages/page1.html")
#except HTTPError as e:
#    print(e)
#else:       #未抛出异常，则执行else
#    if html is None:     #确保服务器存在
#        print("URL is not found")
#    else:
#        bsObj = BeautifulSoup(html.read()) 
          
#        try:                            #假设目标Tag为html.h1
#            badContent = bsObj.html.h1     #若上层Tag为None，会造成AttributeError
#        except AttributeError as e:  #先捕获由于其上层Tag为空可能造成的异常
#            print("Tag was not found")
#        else:
#            if badContent == None:    #再检查目标Tag是否存在
#                print ("Tag was not found")
#            else:
#                print(badContent)   #打印目标Tag



#def fun(de = 10):
#    e = 20
#    print(vars())

#fun()

#def my_range(first = 0, last = None, step = 1):
#    if last is None:   #如果只有一个参数
#        last = first
#        first = 0

#    if first >= last or step < 0:   #参数检查
#        return None

#    temp_num = first
#    while temp_num < last:
#            yield temp_num     #yield类似于return 返回生成器对象
#            temp_num += step

#print(list(my_range(10)))

##my_range()
##print(list(range()))

#def fib(n):  #递归
#    if n == 1:
#        return 1
#    elif n == 2:
#        return 1
#    elif n > 2:
#        return  fib(n - 1) + fib(n - 2)
#    else:
#        print("arg error")

##def fib_generator(num):   #序列生成
##    for x in range(1, num):
##        print(fib(x))

#def fib_generator(num):   #返回list
#    return [x for x in range(1, num)]

#print(fib_generator(7))
        


#def fib(n):  #递归
##    if n == 1:
#        return 1
#    elif n == 2:
#        return 1
#    elif n > 2:
#        return  fib(n - 1) + fib(n - 2)
#    else:
#        print("arg error")


##int('10')
#def called():
#    li = [1, 2, 3]
#    raise ArithmeticError
#    #try:
#    #    li[10]
#    #except IndexError as index:  
#    #    print("called need help!")#输出一些信息，交给调用函数处理  
#    #    raise   #called()函数捕获异常


#def call():
#    try:
#        called()
#    except IndexError as index:   #call()获得called()转发来的异常并进行处理
#        print(index)
#    except ArithmeticError:   #call()获得called()转发来的异常并进行处理
#        print("dsa")

#call()

#class fib:
#    def __init__(self, num):
#        self._num = num

#    def __iter__(self):
#        return self

#    def fib(n):  #递归
#        if n == 1:
#            return 1
#        elif n == 2:
#            return 1
#        elif n > 2:
#            return  fib(n - 1) + fib(n - 2)
#        else:
##            print("arg error")


#class Fab: 
#   def __init__(self, max): 
#       self.max = max 
#       self.n, self.a, self.b = 0, 0, 1 
 
#   def __iter__(self): 
#       return self 
 
#   def next(self): 
#       if self.n < self.max: 
#           r = self.b 
#           self.a, self.b = self.b, self.a + self.b 
#           self.n = self.n + 1 
#           return r 
#       raise StopIteration()

#for n in Fab(5):
#    print(n)

#def fib(n):  #递归
#    if n == 1:
#        return 1
#    elif n == 2:
#        return 1
#    elif n > 2:
#        return  fib(n - 1) + fib(n - 2)
#    else:
#        print("arg error")

#def fib_generator(num):   #fib_generate()函数此时为生成器函数
#    for x in range(1, num):
#        yield fib(x)       #每遇到yield关键字，函数返回数据，但不终止

##for x in fib_generator(7):  #for循环可以遍历函数！！
##        print(x)

#f = fib_generator(7)
#f.next()


#def fun(arg1,  *arg, arg2):   
#    #print(arg1)     
#    #print(arg2)     
#    #print(arg)     

#fun(10, 20, 30 ,40)

#def fun(**kwargs):   #可接受关键字参数并转换为字典
#    print("keywords args:", kwargs)

#fun(value = "hehe", haha = "hehe")   #传参很神奇偶

#def fun(arg1, arg2, arg3 = 10, *args, **kwargs):
#    print(arg1)     
#    print(arg2)     
#    print(args)
#    print(kwargs)  

#fun(10, 20, 30, 40, 50, key = 60)

#def fun(arg1, arg2, arg3 = 10, **kwargs, *args):
#    print(arg1)     
#    print(arg2)     
#    print(args)
#    print(kwargs)  

#fun(10, 20, 30, 40, 50, key = 60)

#def fun(atr):
#    pass

#document_it()函数接受函数名，返回内嵌函数
#该内嵌函数解析并保存传入函数的一些信息


#def fun_outer(arg):
#    def fun_inner():
#        print(arg)   #内部函数可访问外部函数的局部变量
#        print("Test")
#    fun_inner()   #外部函数调用内部函数

#fun_outer(10)

#def fun_outer(arg):
#    def fun_inner():
#        return  "outer_info : " + str(arg)   #内部函数记录外部函数的一些信息
#    return fun_inner   #返回内部函数，不带括号！！

#a = fun_outer(10)   #a, b都是函数，且为闭包函数，此时a函数将会记录此次调用的fun_outer()信息
#b = fun_outer(10)

#print(type(a))  #<class 'function'>  表明其类型为函数
#print(type(b))

#print(a)   #<function fun_outer.<locals>.fun_inner at 0x03ABB978>
#print(b)  #表明其为闭包函数

#print(a())  #输出a()内部函数记录的信息

#def document_it(func):   #*args, **kwargs这种函数表示可以接受三种任意数量参数（位置，关键字，默认值）
#    def new_function(*args, **kwargs):   #内嵌函数，函数内再定义
#        print('Running function:', func.__name__)  #记录传入函数的名字
#        print('Positional arguments:', args)  #记录传入函数的位置参数
#        print('Keyword arguments:', kwargs)  #记录传入函数的关键字参数
#        result = func(*args, **kwargs)   #记录传入函数的运行结果（返回值）
#        print('Result:', result)
#        return result   #返回运行结果
#    return new_function   #返回内嵌函数（新函数）

#def add_ints(a, b):
#    return a + b

#          # 人工对装饰器赋值
##cooler_add_ints = document_it(add_ints)  #cooler_add_ints()成为闭包函数
##cooler_add_ints(3, 5)  

#def cooler_add_ints(*args, **kwargs):
#      print('Running function:', add_ints.__name__)    #这里的func由装饰器赋值时获得，为add_ints
#      print('Positional arguments:', args)  
#      print('Keyword arguments:', kwargs) 
#      result = add_ints(*args, **kwargs)     #注意这里函数调用，func由装饰器赋值时获得，为add_ints
#      print('Result:', result)
#      return result   

#cooler_add_ints(3, 5)    #运行结果一样

##也就是说，装饰器将函数注册进来（形参为函数名），并返回闭包函数给一个新函数
##这个新函数就可以记录注册函数的信息



#def document_it(func):  
#    def new_function(*args, **kwargs):   
#        print('Running function:', func.__name__)  
#        print('Positional arguments:', args)  
#        print('Keyword arguments:', kwargs)  
#        result = func(*args, **kwargs) 
#        print('Result:', result)
#        return result  
#    return new_function   

#def square_it(func):   #平方装饰器
#    def new_function(*args, **kwargs):
#        result = func(*args, **kwargs)
#        return result * result
#    return new_function


##@document_it  #再执行上面的
##@square_it    #先执行靠近函数定义def的装饰器
#def add_ints(a, b):
#    return a + b

#add_ints(3, 5)   

##等价于
#add_ints = square_it(add_ints)   #squre_it()先装饰
#add_ints = document_it(add_ints)   #document_it()后装饰

##squre_it()装饰结果为
#def add_ints(*args, **kwargs):
#    result = a + b  #不是真的 a + b啊！！形象一点而已，因为add_ints已被覆盖了，找不到副本了
#    return result * result

##document_it()装饰结果为
#def add_ints(*args, **kwargs):
#      print('Running function:', add_ints.__name__)   
#      print('Positional arguments:', args)  
#      print('Keyword arguments:', kwargs) 
#      result = (a + b) * (a + b)   #这里的函数调用是squre_it()装饰后的结果，
#                                   #即result * result
#      print('Result:', result)
#      return result   

#add_ints(3, 5)   


#装饰结果为
#def cooler_add_ints(*args, **kwargs):
#      print('Running function:', add_ints.__name__)    #这里的func由装饰器赋值时获得，为add_ints
#      print('Positional arguments:', args)  
#      print('Keyword arguments:', kwargs) 
#      result = add_ints(*args, **kwargs)     #注意这里函数调用，func由装饰器赋值时获得，为add_ints
#      print('Result:', result)
#      return result   



#          # 人工对装饰器赋值
##cooler_add_ints = document_it(add_ints)  #cooler_add_ints()成为闭包函数
##cooler_add_ints(3, 5)  

#def cooler_add_ints(*args, **kwargs):
#      print('Running function:', add_ints.__name__)    #这里的func由装饰器赋值时获得，为add_ints
#      print('Positional arguments:', args)  
#      print('Keyword arguments:', kwargs) 
#      result = add_ints(*args, **kwargs)     #注意这里函数调用，func由装饰器赋值时获得，为add_ints
#      print('Result:', result)
#      return result   

#cooler_add_ints(3, 5)    #运行结果一样

##也就是说，装饰器将函数注册进来（形参为函数名），并返回闭包函数给一个新函数
##这个新函数就可以记录注册函数的信息

##至于怎么用这个闭包函数，取决于闭包的实现
##上面例子中闭包函数调用了注册函数，则可以像注册函数那样使用闭包函数
##如果没调用注册函数，那就是一个普通的闭包函数，仅记录一些信息而已

#def fun_outer(arg):
#    def fun_inner():
#        print(arg)   #内部函数可访问外部函数的局部变量
#        print("Test")
#    fun_inner()   #外部函数调用内部函数
#    print(x)   #外部不可访问内部，很好理解


#fun_outer.


