# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 15:43:20 2021

@author: LiFish
"""
import requests
from bs4 import BeautifulSoup
def get_T(): #爬蟲獲得天氣資料
    url = "https://weather.yam.com/%E6%96%B0%E8%8E%8A%E5%8D%80/%E6%96%B0%E5%8C%97%E5%B8%82"
    html = requests.get(url)
    html.encoding = "utf-8"
    bs = BeautifulSoup(html.text, "lxml")
    item = bs.find("div",{"class":"tempB"})
    item2 = bs.find("div",{"class":"direc"})
    item3 = bs.find("div",{"class":"wind"})
    item = str(item) ; item2 = str(item2) ; item3 = str(item3)
    item = item[45:47] ; item2 = item2[19:22] ; item3 = round(float(item3[18:23].strip("km/h"))*0.278,2)
    x = a(item2)
    return item ,x,item3

def a(x): #判斷風向
    s = "" ;a = 0
    for i in x:
        if i == "東":
            s += "E" ; a+= 1
        elif i == "西":
            s += "W" ; a+= 1
        elif i == "北":
            s += "N" ; a+= 1
        elif i== "南":
            s += "S" ; a+= 1
    if a ==0:
        s ="X"
    return s


def recommended(x): #推薦放飛程度
    x = int(x)
    if x < 5:
        return "High",53,245,107
    elif x < 10:
        return "Middle",195,195,195
    else:
        return "Low",246,59,66
