# 算出图结构基础数据
from gensim import corpora, models, similarities
import logging
import csv
import re
from nltk.corpus import stopwords
from getCsv import getCsvByfilePath
from getls import getls
import time
import os
import psutil

#startTime = time.time()

def tu_structure(projectName_Write,readString,file_list,Write_path):
    writeResult = {}
    k=0
    for comparing_file_name in file_list:
        resultList = getls(readString, comparing_file_name, k)
        print(len(resultList))
        writeResult[k] = resultList
        k += 1
        #print(resultList)
    #print(writeResult)
    s = str(writeResult)
    f = open(Write_path+'_dict.txt', 'w')
    f.writelines(s)
    f.close()
    print(len(writeResult))
#print('程序运行所需时间为: %.4f sec' % (time.time() - startTime))
#print('当前进程的内存使用：%.4f MB' % (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024))
