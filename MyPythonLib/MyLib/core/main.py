#-*-coding:utf-8-*-

import pro_init
pro_init.sys_path_append()   #新建project后记得附加路径

from core.net.HTML_analyze import get_tag

#get_tag.get_tag("http://www.pythonscraping.com/pages/warandpeace.html","html")

from urllib.request import urlopen
from  bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

for child in bsObj.find("table",{"id":"giftList"}).children:
    print(child)

#print(bsObject.prettify())

#nameList = bsObject.findAll(text="the prince")
#print(len(nameList))
#for name in nameList:
#    print(name.get_text())

#from urllib.request import urlopen
#from bs4 import BeautifulSoup
#html = urlopen("http://www.pythonscraping.com/pages/page3.html")
#bsObj = BeautifulSoup(html)
#for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
#    print(sibling, end = "")


from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"
        }).parent.previous_sibling.get_text())




