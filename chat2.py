# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 01:49:32 2022
@author: JYH
"""

# 本次學習重點：list 分割算對話紀錄中字數統計, 拆解空格，不同欄之間分區統計.
# python 的none 與c 的 null 差異？

import os


#讀取檔案: with open, 搭配utf-8-sig code, 把對話內容以for loop append into lines
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines #上方只完成print proudct, 還需要把值return到product
    

# convert: 以名字區分，將上面list "lines"中對話內容中空白鍵先去除，再把時間，名字，對話內容分別
def convert(lines):
    new = []
    person = None
    allen_word_count = 0 # []跟0，跟null的差別? '', [],0,none在boolean上都是false
    allen_sticker_count = 0
    allen_image_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_count = 0
    for line in lines: 
        s = line.split(' ') 
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count +=1
            else:
                for m in s[2:]: #存在於對話內容中的所有內容：從第column 2之後都是
                   allen_word_count += len(m) #把allen說的內容字元數加總
                   # print('here is what Allen said',m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else:
                for m in s[2:]:
                    viki_word_count += len(m) #把viki說的內容字元數加總
                    # print('here is what Viki said',m)
    print('Allen 說了', allen_word_count, '個字')
    print('Allen 傳了', allen_image_count, '個圖片')
    print('Allen 傳了', allen_sticker_count, '個貼圖')
    print('Viki 說了',  viki_word_count, '個字')
    print('viki傳了', viki_image_count, '個圖片')
    print('viki傳了', viki_sticker_count, '個貼圖')
    return new


#寫入檔案
def write_file(filename, chat):
   with open(filename, 'w', encoding = 'utf-8') as f:
         #f.write('商品' + ',' + '價格' + '\n') 
        for r in chat:
            f.write((r[0]) + ':' + (r[1]) + '\n') #prices were int and csv file context is divided with comma
            #f.write(r + '\n')


######################本文開始##################################

def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)
    # write_file('output_teacher.txt', lines)

main()
    
