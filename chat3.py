# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 17:07:16 2022

@author: user
"""
# 本次學習重點：用list方法一樣可分割str, .
# output: python 的none 與c 的 null 差異？
# extension: list/string/dictionary 3個python基本操作, tutle??

lines = []
with open('chat3.txt', 'r', encoding = 'utf-8-sig') as f:
    for line in f:
        lines.append(line.strip())
        
for line in lines:
    s = line.split(' ')
    time = s[0][0:5] #把s第1個column中前0~4個digit取出, 因str屬於list，可用list的方法
    name = s[0][5:]  #把s第1個column中第5個digit之後取出
    print(time)
    print(name)