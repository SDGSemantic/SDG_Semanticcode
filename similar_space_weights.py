#计算相似空间权值总和（SSW）
import os
import numpy as np
import  csv
#1.获取每个文件与其相似的文件的字典
with open(Write_path+'_dict.txt', "r") as f:  # 打开文件
    graph_dict = f.read()
graph_dict = eval(graph_dict)
#获取相似矩阵

# 数据文件转矩阵
# path: 数据文件路径
# delimiter: 行内字段分隔符
#2.将txt里的内容转换为矩阵形式
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


def SSW(Write_path):
    recordArray = file2array(Write_path + '_matrix_reflection.txt', ' ')  # 文件到矩阵的转换
    c = recordArray.tolist()
    # 打开all_files_connected_vertexs_0.8.csv开始计算
    file = open(Write_path + "_all_files_connected_vertexs.csv", 'r')
    files_node = csv.reader(file)

    for file in files_node:
        sum = 0
        str1 = ""
        k = int(file[0])
        list_nodes = eval(file[2])
        for list_node in list_nodes:
            value = graph_dict[list_node]
            if len(value) == 0: continue
            for i in value:
                sum += float(c[list_node][i])
        str1 += str(round(sum, 2)) + "\n"
        print(str1)
        with open(Write_path + "_similar_space_weight.csv", "a", encoding='utf-8', newline='') as f:
            f.writelines(str1)
