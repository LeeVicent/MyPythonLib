class MyClass:     #类定义
    def __init__(self, a, b):    #默认值构造方法定义
        self._a = a    #数据成员定义   

    def __init__(self, value = 20):    #默认值构造方法定义
        self._value = value    #数据成员定义  
         
    def set_value(self, value):    #赋值方法
        self. _value = value

    def get_value(self):    #取值方法
        return self._value

    def __str__(self):   #状态表示方法    #类似DisPlay方法
        return "vlaue = " + str(self._value)   #一般都是返回str