# 将多个csv文件按列合并为一个csv
import pandas as pd
import csv

def All_Metrics(Write_path):
    inputfile_csv_1 = Write_path+"_filename_metric.csv"
    inputfile_csv_2 = Write_path+"_all_files_longest_path.csv"
    inputfile_csv_3 = Write_path+"_all_files_connected_vertexs.csv"
    inputfile_csv_4 = Write_path+"_similar_distance.csv"
    inputfile_csv_5 = Write_path+"_similar_space_weight.csv"
    csv_1 = pd.read_csv(inputfile_csv_1)
    csv_2 = pd.read_csv(inputfile_csv_2, usecols=[1])
    csv_3 = pd.read_csv(inputfile_csv_3, usecols=[1])
    csv_4 = pd.read_csv(inputfile_csv_4)
    csv_5 = pd.read_csv(inputfile_csv_5)
    # 拼接文件
    out_csv = pd.concat([csv_1, csv_2, csv_3, csv_4, csv_5], axis=1)
    out_csv.to_csv(inputfile_csv_1, index=False)

    r = csv.reader(open(inputfile_csv_1, 'r'))
    newFile = open(Write_path+'_tmp.csv', 'w')
    w = csv.writer(newFile)

    # 将计算的两列写入到新文件中
    for row in r:
        print(row[1])
        a = float(row[8]) / float(row[7])
        b = float(row[9]) / float(row[7])
        w.writerow([a, b])
    newFile.close()

    # 将新文件添加到原文件中
    csv_1 = pd.read_csv(inputfile_csv_1)
    csv_6 = pd.read_csv(Write_path+'_tmp.csv', usecols=[0, 1])
    out_csv1 = pd.concat([csv_1, csv_6], axis=1)
    out_csv1.to_csv(inputfile_csv_1, index=False)