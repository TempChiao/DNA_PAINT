# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os

def init():
    fp = (r"/Volumes/Tianxiao/20231027_Tx_TDP_CSF/")
    print_dirs(4, fp)

def print_dirs(step, fp):
    print('\n\n')
    count = 0
    done = []
    for root, dirs, files in os.walk(fp):
        for name in files:
            if step == 1:
                if 'posZ0.tif' in name:
                    for_ij = r'path[{0}]="{1}\";'.format(count, root)
                    if root not in done:
                        done.append(root)
                        print(for_ij.replace('\\', '/'))
                        count += 1
            elif step == 2:
                if 'FitResults.txt' in name:
                    for_py = 'pathList.append(r"{0}")'.format(root)
                    print(for_py)
            elif step == 3:

                if '.png' in name:
                    for_latex = r'.newpage \r .begin\{figure\}\[hbtp\] \r.centering \r.includegraphics[width=1\textwidth]\{{0}.png\}\r.end\{figure\}\r.newpage\{0\}'.format(count)
            
                    print(for_latex)
                    
                    count += 1
            elif step == 4:
                if 'FitResults.txt' in name:
                    if '_' not in name:
                        for_py = 'pathList.append(r"{0}/")'.format(root)
                        print(for_py)
                        #print name
            elif step == 5:

                if 'Raw' in name:
                    for_igor = r'filelist[{0}]="{1}\"'.format(count, root)
                    for_igor = for_igor.replace('/',':')
                    for_igor = for_igor.replace(':Users','Macintosh HD:Users')
                    print(for_igor.replace('\\', ':'))
                    count+=1
init()