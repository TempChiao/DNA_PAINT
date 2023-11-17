#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 10:50:56 2023

@author: tempchiao
"""

#画二维坐标图
#读取csv并作图
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

# with open("/Users/tempchiao/UofE/TEST/2uM_1in10_1nM_Apt_1.csv", 'r') as file:
#   csvreader = csv.reader(file)
#   csvreader.replace('\\t','\'\'')
#   for row in csvreader:
#     print(row)
ls = []
readData = pd.read_csv("/Volumes/Tianxiao/20230725_Tx_FUS_Best test/CSV_10uM_Apt1_1nM/merge.csv",header= None,sep='\\t')   #读取csv数据
# print(readData)
area = readData[1]
for i in area:
    ls.append(i)
a = len(ls)
print(a)
print(sorted(ls))
# print(ls)
# data = readData.iloc[:,2].tolist()       #获取dataFrame中的第3列，并将此转换为list
# xData = list(range(1,len(data)+1))       #产生横轴坐标
 
# plt.plot(xData, data,'r-^')              #画散点图，*:r表示点用*表示，颜色为红色
# plt.title("time-distance")               #设置标题
# plt.xlabel("time-500ms")                 #横轴名称
# plt.ylabel("distance")                   #纵轴名称
# plt.show()                               #画图
# xdata = area
xdata = sorted(ls)
ydata = readData[11]
plt.plot(xdata, ydata, 'r-^')
plt.show()
print(readData[11])

# ratio=readData['Number_of_locs']
# plt.hist(ratio, bins = 10,range=[0,300], rwidth=0.9,color='#ff0000')
# plt.xlabel('Eccentricity',size=20)
# plt.ylabel('Number of Features',size=20)
# plt.title('Cluster Eccentricity',size=20)
# # plt.savefig(path+"Ecc.pdf")
# plt.show()