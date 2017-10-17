'''
关键字屏蔽
关键字来源于文件，被替换为*
关键字来源文件中的关键字以换行作为分隔
'''
#!/usr/bin/env python
# encoding: utf-8
__author__ = 'Vicent'

import os

def key_block(fileName):
    if os.path.isfile(fileName):
        file = open(fileName, 'r')
    else:
        print("dstFile doesn't exist!")
    li = [x.strip() for x in file]   #每行后面有换行符，得先去掉'\n'
    flag = 0
    while 1:
        word = input('please input str:')
        for x in li:
            if word.find(x) != -1:   #找到
                print(word.replace(x, '*'))
                flag = 1
                break
        if flag == 0:
            print(word)