import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import urllib.parse
from urllib import request, response, error, parse
from urllib.request import urlopen
import re
import requests

from urllib.request import urlopen
from bs4 import BeautifulSoup

#try:
#    html = urlopen(url)

#except error.HTTPError as e:
#     print(req.headers)
#    print (e.reason, e.code, e.headers, sep = '\n')

def pageturning1():
    f = open("celebrity.txt", "w+")
    i = 0
    while i>=0 :
        i += 1
        url_i = "http://www.1905.com/mdb/relation/list/" + "s1t0p" + str(i) + ".html"
        print(url_i)
        referer = url_i
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
        headers = {'User-Agent': user_agent, 'Referer': referer, 'Connection': 'keep-alive'}
        try:
            req = urllib.request.Request(url = url_i, headers = headers)
            response = urlopen(req)
            html = response.read()
            print(i)
        except error.HTTPError as e:
            break
        soup = BeautifulSoup(html, "lxml")
        page = soup.find_all(id = "new_page")

        #检查是否有下一页
        #如果有，调用relations打印数据，如果没有，break后回到while loop翻页
        for p in page:
            allp = p.find_all('a', href = True)
            for x in allp:
                if x.get_text() == "下一页":
                    print("Still pages left, keep going!")
                    #print(relations(soup))
            if x['href'] == "/mdb/relation/list/s1t0p" + str(i+1)+ ".html":
                break
            else:
                i = -1
        f.write(relations(soup))
        print(relations(soup)) # 打印数据

    print("已经到达最后一页")

    return



# get celebrity relations by filtering into specific div,ul and li
def relations(soup):
    #page = soup.find_all('div',  class_ = "new-page")
    #print(page)
    k = soup.find_all('div', class_='gx_List mt10')
    for x in k:
        allP = x.find_all('ul')
        for person in allP:
            result = ""
            for el in person.find_all('li'):
                iD = ""
                for a in el.find_all('a', href = True):
                    p = el.get_text("|", strip = True)
                    iD += a['href']
                    iD += "|"
                res = p + iD #一条关系 加上对应的id
                res += "\n" #一条结束后换行
                result += res
            return result


pageturning1()
