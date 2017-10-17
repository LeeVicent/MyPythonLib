'''
作为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 10 个激活码（或者优惠券）？
'''

#!/usr/bin/env python
# encoding: utf-8
__author__ = 'Kxrr'

import random, string

ALL_LETTERS = string.ascii_uppercase + string.digits  #生成一个字符串，包含26字母与10个阿拉伯数字
codeAmount = 10
codeRound = 10
codeResult = []

while len(codeResult) != codeAmount:
     everyCode =''.join((random.choice(ALL_LETTERS) for i in range(codeRound)))  #元组生成
     if everyCode not in codeResult:  #去重
        codeResult.append(everyCode)

print("验证码数量为：" + str(len(codeResult)) + "\n")

# codeResult 结果为一个超长列表，改为每5个换行输出
count = 1
for x in codeResult:
    print(x, end=' ')
    count += 1
    if count % 5 == 1:    #Python 不支持 if  表达式内写赋值语句
        print('\n')
