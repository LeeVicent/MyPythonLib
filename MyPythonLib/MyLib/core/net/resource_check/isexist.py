#此模块用于检查各种网络数据是否存在
#存在则返回html对象
#-*-coding:utf-8-*-

from urllib.request import urlopen   # 导入urlopen函数
from urllib.error import HTTPError
from bs4 import BeautifulSoup    # 导入BeautifulSoup类

def isexist(resource_name, resource_type):   #str, str
    if resource_type.lower() == "url":
        try:          # 确保网页在服务器上存在
            html = urlopen(resource_name)
        except HTTPError as e:  
            print(e, sep = '')
            print("----url_check")
            return None
        else:
            if html is None:   # 确保服务器存在
                print("severs don't exist!----url_check")
                return None
            else:
                return html


    