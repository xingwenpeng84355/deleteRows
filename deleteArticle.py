#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 22:33:37 2020

@author: xingwenpeng
"""

import csv
import pandas as pd


path0 = "/Users/xingwenpeng/Desktop/agg_doc_vecs.csv"
fh = open(path0, encoding='utf-8')   # 要检测文章的路径
data = csv.reader(fh)  # 打开文章
i=0
ID=[1,2,3,4] #要删除的序号
doc=[]
for row in data:
    i=i+1
    if i not in ID:
        doc.append(row)#把不需要删除的文章加进去
       # print(i)
        
        
df = pd.DataFrame(doc)