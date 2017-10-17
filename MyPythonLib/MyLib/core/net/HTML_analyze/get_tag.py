'''
本模块用于解析目标网站的特定HTML标签

[使用范例]：
from core.net.HTML_analyze import get_tag
get_tag.get_tag("http://www.taobao.com","title")
'''


from urllib.error import HTTPError
from bs4 import BeautifulSoup  
from core.net.resource_check import isexist

def get_tag(url_address, tag_type):
    print("url address: " + url_address)
    print("tag type: " + tag_type)
    print("analyzing...")

    html = isexist.isexist(url_address,"url")
    print("analyz success!")
    if html is None:
        return None;
    else:
        #使用BS库解析HTML文档   #删掉"html.parser"可看到库作者的警告文字
        bsObj = BeautifulSoup(html.read(), "html.parser") 

        #虽然可以直接写title，但是需要写全，因为展开层级中前面的可能会抛出异常
        switch = {
            "html" : lambda  : bsObj.html,
                "head" : lambda  : bsObj.html.head,
                    "title" : lambda  : bsObj.html.head.title,
                "body" : lambda  : bsObj.html.body,
                    "h1" : lambda  : bsObj.html.body.h1,
                    "div" : lambda  : bsObj.html.body.div
            }

        try:                         
            #假设目标Tag为html.h1
            #若上层Tag为None,会造成AttributeError
            badContent = switch[tag_type]()    
        except AttributeError as e:        #上层为None
            print("OverTag was not found")   
        except KeyError as key:    #switch不匹配
            print("get_tag() function doesn't exist the taget tag!!")
        else:
            if badContent == None:    
                print ("TagertTag was not found")   #目标层为None
            else:
                print(badContent.get_text())  #get_text()去掉标记

               
#由于函数调用不可拼接，所以需要switch-case调用  

