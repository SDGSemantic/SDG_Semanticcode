#计算相似空间距离（SSD）

import os
import numpy as np
import csv
# 数据文件转矩阵
# path: 数据文件路径
# delimiter: 行内字段分隔符
#1.将txt里的内容转换为矩阵形式
def file2array(path, delimiter):
    recordlist = []
    fp = open(path, 'r', encoding='utf-8')
    content = fp.read()  # content现在是一行字符串，该字符串包含文件所有内容
    fp.close()
    rowlist = content.splitlines()  # 按行转换为一维表，splitlines默认参数是‘\n’
    # 逐行遍历
    # 结果按分隔符分割为行向量
    recordlist = [row.split(delimiter) for row in rowlist if row.strip()]
    return np.array(recordlist)

def SSD(Write_path):
    recordArray = file2array(Write_path + "_matrix_reflection.txt", ' ')  # 文件到矩阵的转换
    c = recordArray.tolist()
    file = open(Write_path+'_all_files_connected_vertexs.csv', 'r')
    # 读取active_file.csv文件内容
    files_node = csv.reader(file)

    for file in files_node:
        # sum:每个文件的相似空间距离
        sum = 0
        str1 = ""
        num1 = int(file[0])
        file[2] = eval(file[2])
        for i in file[2]:
            if i != num1:
                sum += float(c[num1][i])
        str1 += str(round(sum, 2)) + "\n"
        with open(Write_path+"_similar_distance.csv", "a",encoding='utf-8', newline='') as f:
            f.writelines(str1)


