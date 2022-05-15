# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 01:49:32 2022
@author: JYH
"""

import os


#讀取檔案
def read_file(filename):
    chat = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        person1 = input('Please key in person1:')
        person2 = input('Please key in person2:')
        for line in f:
            if person1 in line or person2 in line: #why == substitude in would fail?
                 person = line.strip()
                 continue
            context = line.strip()
            chat.append([person, context]) #此型式chat為list
            #chat.append(person + ':' + context) #此型式chat為list
    print(chat)
    print(type(chat))
    print(type(chat[0][0]))
    print(type(chat[0][1]))
    return chat #上方只完成print proudct, 還需要把值return到product
    


# =============================================================================
# products = []
# with open('product2.csv', 'r', encoding = 'utf-8') as f:
#     for line in f:
#         if '商品, 價格' in line:
#             continue
#         name, price = line.strip().split(',') # strip \n and then split comma
#         products.append([name, price])      
# print(products)
# =============================================================================

# =============================================================================
# #使用者輸入商品到一個已存在的檔案
# def user_input(product):
#     while True:
#         name = input('Please key in product names:')
#         if name == 'q':
#             break
#         price = input('Please key in price:')
#         price = int(price) #input 輸入context為str, 轉成int方便之後運算
#         product.append([name, price]) # add p into product list
#     print(product)
#     return product
# =============================================================================


# =============================================================================
# ##印出購買紀錄
# def print_product(product):
#     for q in product:
#         print(q[0],'price is:', q[1])
# =============================================================================


#write product into a string file txt    


#寫入檔案
def write_file(filename, chat):
   with open(filename, 'w', encoding = 'utf-8') as f:
         #f.write('商品' + ',' + '價格' + '\n') 
        for r in chat:
            f.write((r[0]) + ':' + (r[1]) + '\n') #prices were int and csv file context is divided with comma
            #f.write(r + '\n')


######################本文開始##################################

def main():
    filename = 'chat.txt'
    if os.path.isfile(filename): #check file exist or not
            print('found it!')
            chat = read_file(filename)
    else:
            print('could not find the file')
            
    write_file('output3.txt', chat)
    

main()