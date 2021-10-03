# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 16:53:04 2021

@author: LiFish
"""
def get(x,d):
    s = ""
    if 37 <= x <43:
        s += '40'
    elif 43 <= x <47:
        s += '45'
    elif 47 <= x < 53:
        s += '50'
    elif 53 <= x < 57:
        s += +'55'
    elif 57 <= x <63:
        s += '60'
    for i in d:
        if i =="E":
            s+='e'
        elif i == "W":
            s+= 'w'
        elif i == "N":
            s+= 'n'
        elif i == "S":
            s += 's'
    return s
#print(get(43.586,"EN"))

def location_name(x):
    if x == "40e":
        return "Shuangxi District,New Taipei City"
    elif x == "40es":
        return "Jiaoxi Township, Yilan County"
    elif x == "40s":
        return"Fuxing District, Taoyuan City"
    elif x == "40ws":
        return"Xionglin Township, Hsinchu County"
    elif x == "45e":
        return"Shuangxi District,New Taipei City"
    elif x == "45es":
        return"Zhuangwei Township, Yilan County"
    elif x == "45s":
        return"intersection of Taoyuan City and Yilan County"
    elif x == "45ws":
        return "Zhudong Township, Hsinchu County"
    elif x == "50e":
        return"Gongliao District,New Taipei City"
    elif x == "60es":
        return"None"
    elif x == "60s":
        return"None"
    elif x == "60ws":
        return"None"
    else:
        return "Ocean"
