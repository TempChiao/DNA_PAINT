#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 13:35:02 2023

@author: tempchiao
"""

import os

operate_path="/Volumes/Tianxiao/20231027_Tx_TDP_CSF"
n = 0
for root, dirs, files in os.walk(operate_path):
    if dirs == []:
        '''if files[:][-9:] == 'posZ0.tif':'''
        for i in files:
            if i[-9:] == 'posZ0.tif':
                # print('"'+root+'/'+i[:-4]+'"',end='\n\n')
               print('path['+str(n)+']=''"'+root+'/'+'"',end='\n\n')
               n = n + 1
        
        # print('root:',root)
        # print('dirs:',dirs)
        # print('files:',files[-1][-3:])
        # print('\n')
        
        # '''if files[:][-9:] == 'posZ0.tif':'''
        # for i in files:
        #     if i[-9:] == 'posZ0.tif':
        #         print('"'+root+'/'+i[:-4]+'"',end='\n\n')