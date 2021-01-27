# 算出文本之间的相似度
from gensim import corpora, models, similarities
import logging
import csv
import re
from nltk.corpus import stopwords
from getCsv import getCsvByfilePath
from getls import getls
from tu_structure import tu_structure
from file_indexs import file_indexs
from Similarity_matrix import Similarrity_Matrix
from similar_space_eight import SSW
from Similar_spatial_distance import SSD
from Combine_all_metrics import All_Metrics
import time
import os
import psutil

#startTime = time.time()

if __name__ == '__main__':

    projectName_Write = "xerces1.2"
    projectName = "xerces-1.2.0-src"
    readString = "C:\\Users\\sherlock\\Apach\\" + projectName_Write + "_data\\" + projectName_Write + "_filename.csv"
    writeString = "C:\\Users\\sherlock\\Apach\\" + projectName_Write + "_data\\" + projectName_Write + "_filename_metric.csv"
    udb_path = "C:\\Users\\sherlock\\Apach\\" + projectName + "\\" + projectName + ".udb"
    Write_path="C:\\Users\\sherlock\\Apach\\" + projectName_Write + "_data\\" + projectName_Write
    # 1.获取所有文件名放入list中
    file_list = []
    with open(readString, "r") as f:
        file_content = csv.reader(f)

        for file in file_content:
            filePath = file[0]
            if not filePath[-4:] == "java":
                continue
            file_list.append(filePath)
        print(file_list)

    # 2.创建每个文件的csv
    count = 0
    for file_path in file_list:
        count += 1
        print(count)
        #if count < 25200:
            #continue
        getCsvByfilePath(udb_path, file_path)

   # 3.将每个文件与其余文件作比较得SDW,DC，ADW,SSS,SSA指标

    writeResult = []
    for comparing_file_name in file_list:
        resultList = getls(readString, comparing_file_name)
        print(resultList)
         # 输出文件名，相似度和，平均相似度
        if not resultList == []:

            if resultList[1]==0:
                writeResult.append([comparing_file_name, 0, 0, 0, round(resultList[2], 2),round(resultList[2] / (resultList[3]), 2)])
                continue
            writeResult.append([comparing_file_name, round(resultList[0], 2),
                               resultList[1], round(resultList[0] / (resultList[1]), 2), round(resultList[2], 2),round(resultList[2] / (resultList[3]), 2)])

    with open(writeString, "a", encoding='utf-8', newline='') as f:
       writer = csv.writer(f)
       for wr in writeResult:
        writer.writerow(wr)
    #4.得到图结构
    tu_structure(projectName_Write,readString,file_list,Write_path)

    #5得到LDP（MSD）和ISF（NSSF）指标
    file_indexs(Write_path)

    #6计算相似矩阵
    Similarrity_Matrix(Write_path, readString, file_list)

    #7计算指标SFW（SSD）
    SSD(Write_path)

    #8计算指标ISW
    SSW(Write_path)

    #9 得到指标AWIS，AFW(MDSS,AWDSS)并得到最终指标
    All_Metrics(Write_path)



#print('程序运行所需时间为: %.4f sec' % (time.time() - startTime))
#print('当前进程的内存使用：%.4f MB' % (psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024))
