#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:56:54 2020

@author: chengeorge
"""

#cars=['toyato','bmw','bize']
#search_car='bmw'
#i=cars.index(search_car)
#print("搜尋的 %s 出現的第一個索引在 %d" % (search_car , i))

#ch6_34.py
#james=['Lebor',23,45,11,31,18]
#games=len(james)
#score_Max=max(james[1:games])
#i=james.index(score_Max)
#print(james[0],"第 %d 得最高分 %d" % (i, score_Max))

#ch6_56
#drinks=["coffee","tea","wine"]
#enumerate_drinks=enumerate(drinks)
#print(enumerate_drinks)
#print(type(enumerate_drinks))

#ch7_3
#players=['curry','jordon','jemes','george']
#py=[]
#for person in players[:3]:
#    print(person.title())
#    if person.startswith('j'):
#        py.append(person)
#print(py)
#string=[1,2,4]
#for i in dir(string):
#    print(i)

#ch7
#n =int(input("請輸入數量："))
#for num in range(n):
#    print("*",end="\n4")
#       

#total=sum(range(n+1))
#print(total)
#
#oddlist=[num for num in range(1,10) if num %2 ==1]
#print(oddlist)
#
#X=[[a,b,c] for a in range(1,20) for b in range(a,20) for c in range(b,20) if a**2+b**2==c**2]
#print(X)

#ans=30
#guess =0
#while guess!=ans:
#    guess=int(input("guess a number!"))
#    if guess > ans:
#        print("must low")
#    elif guess <ans:
#        print("must bigger")34
#    else:
#        print("its right")
#    
#scores=[21,45,23,66,34,17,65,33]
#for count,score in enumerate(scores,1):
#    if score>23:
#        print("test %d %d" % (count,score))
#    

#ch10-32
#A={'a','b','c','d'}
#B={'a','k','c'}
#C={'c','f','w'}
#ret_value=A.intersection_update(B)
#print(ret_value)
#print(A)

#def build_vip(id,name,tel=''):
#    vip_dict={'VIP_UD':id,'Name':name}
#    if tel: #重點
#        vip_dict['Tel']=tel
#    return vip_dict
#
#member1=build_vip('101','george')
#member2=build_vip('102','cat','23880600')
#print(member1)
#print(member2)

#ch11_22
#def inserChar(letter,myList=[],inList=[1,2]):
#    myList.append(letter)
#    inList.append(letter)
#    print(myList)
#    print(inList)
#inserChar('x')
#inserChar('y')
#
#def inserChar(letter,myList=None):
#    if myList==None:
#        myList=[]
#    myList.append(letter)
#    print(myList)
#    
#inserChar('x')
#inserChar('y')

#ch11_25
#def total(data):
#    return sum(data)
#x=(1,5,4)
#myList=[min,max,sum,total]
#
#for f in myList:
#    print(f,f(x))
#    
#def outer(a,b):
#    def inner(x):
#        return a*x+b
#    return inner
#f1=outer(3,2)
#print(f1)
#print(f1(3))asfycs

#import sys
#print(sys.version_info)
#print("please input",end ="")
#msg=sys.stdin.readline(8)
##print(msg)
#print(sys.platform)
#for dirpath in sys.path:
#    print(dirpath)

#from collections import Counter
#fruitsdict=["apple","orange","apple"]
##print(Counter(fruitsdict))
#word ='deep learning'
#alcounter={al:word.count(al) for al in set(word)}
#print(alcounter)
#print(set(word))

import re
msg = '''02-3223323,(02)-26699999,02-2999999 ext 123,
    12345678,02 23880600 ext.350'''
pattern = r'''(
            (\d{2}|(d{2}\))?
            (\s|-)?
            \d{8}
            (\s*(ext|ext.)\s*\d{2,4})?
            )'''
phoneNUm=re.findall(pattern,msg)