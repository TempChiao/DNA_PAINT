#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 09:57:41 2023

@author: tempchiao
"""
import matplotlib.pyplot as plt

import pandas as pd

import numpy as np

import csv

import os

# read data from csv file and return a list

def get_data(path,column):
    print(path)
    ls = []
    readData = pd.read_csv(path,sep='\\t', header=None)
    a = readData[column]
    for i in a:
        ls.append(i)
    lenth = len(ls)
    return ls, lenth




# plot data 

# def plot_data(x,y,x_name,y_name,save_path):
#     # colors of the plot, symmetric from middle
#     colors = []
#     for i in range(int(len(x) / 2)):
#         colors.append([i / int(len(x)/2), 0.5, 0.5])
#     colors = colors + colors[::-1]
#     plt.bar(x,y,color=colors,width = 50)
#     plt.xlabel(x_name,size=20)
#     plt.ylabel(y_name,size=20)
#     plt.savefig(save_path+x_name)
#     plt.show()


def plot_his(zzzzz):
    
    # colors = []
    # for i in range(int(len(zzzzz) / 2)):
    #     colors.append([i / int(len(zzzzz)/2), 0.5, 0.5])
    # colors = colors + colors[::-1]
    plt.figure(figsize = (9, 6), dpi = 300)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=18)
    plt.hist(zzzzz, bins = 30,range=[0,2500],color = '#ff0000', rwidth=0.9,density=1)      #bin stands for how many bins the data would be divided into
    # plt.xlabel('Area',size=26)
    # plt.ylabel('Number of aggregates',size=26)
    
    # plt.title('Cluster Eccentricity',size=20)
    plt.savefig(save_dir[flag]+'Area')
    plt.show()
    return zzzzz
    

# find path of csv file and the path of the folder of csv file.

def find_csv(operate_path):
    csv_dir = []
    folder_dir = []
    for root, dirs, files in os.walk(operate_path):
        if 'CSV_' in root:
            for i in files:
               if '._' not in i: 
                   if 'merge.csv' in i:
                        a = root + '/' + i
                        b = root + '/'
                        csv_dir.append(a)
                        folder_dir.append(b)
    return csv_dir, folder_dir


operate_path = '/Volumes/Tianxiao/20230725_Tx_FUS_Best test/'

path, save_dir = find_csv(operate_path)

lie = 1                     #change here to change the column to be drawn

shu, length = get_data(path[0],lie)

# plot_his(shu)
# # plt.hist(shu, bins = 30,range=[0,1500],color = '#ff0000', rwidth=0.9,density=1)
# plt.show()

flag = 0
for i in path:
    data, length = get_data(path[flag],lie)
    plot_his(data)
    # plt.savefig(save_dir[flag]+'Number of localization')
    flag += 1 

# data,lenth = get_data(path, column)
# data_2, data_3 = get_data(path, 'Number_of_locs')
# plot_data(data,data_2, 'x_name', 'y_name')
# print(data)
# print(lenth)
