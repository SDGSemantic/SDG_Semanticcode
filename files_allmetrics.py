# 程序功能： 将每个功能的各个指标算出

import re
import csv
import pandas as pd

# 1.生成一个新的包含每个功能指标的csv文件
projectName_Write = "xerces1.3"
# 旧的指标所在，新的指标所在，bug_java_file所在
fileRoot = "C:\\Users\\sherlock\\Apach\\" + projectName_Write + "_data\\"
new_fileRoot = "C:\\Users\\sherlock\\Apach\\project_semantic_SSS_SSA\\"
fileRoot1 ="C:\\Users\\sherlock\\Apach\\" + projectName_Write + "_data\\"

with open(new_fileRoot+projectName_Write+"_semanticmetrics.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Filename','SSS','SSA','SDW','DC', 'ADW','MSD', 'NSSF', 'SSD',"SSW",'MDSS','AWDSS',
                     'Bugrate','classify'])

#打开原来旧的指标csv
file = open(fileRoot+ projectName_Write + "_filename_metric.csv", 'r')
# 读取文件内容
javafiles = csv.reader(file)
#计算出每个文件的bugrate
for file in javafiles:
    result=[0,0,0,0,0,0,0,0,0,0,0,0,0]
    '''
    bugrate = 0
    t1 = file[0].replace('\\', '/')
    print(t1)
    f = open(fileRoot1+projectName_Write+'_bug_file.csv', 'r')
    bug_javafiles = csv.reader(f)
    for bug_file in bug_javafiles:
        if re.search(bug_file[0].replace(")", ""), t1):
            bugrate += 1
   '''
    result=[file[0],file[1],file[2],file[3],file[4],file[5],file[6],file[7],file[8],file[9],file[10],file[11],file[12]]
    with open(new_fileRoot+projectName_Write+"_semanticmetrics.csv", "a", encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(result)

# 2.按照bugrate的值从大到小排序
df = pd.read_csv(new_fileRoot + projectName_Write + "_semanticmetrics.csv")
df = df.sort_values('Bugrate', ascending=False)
df.to_csv(new_fileRoot + projectName_Write + "_sort_semanticmetrics.csv", index=False)
'''
# 3.标注每个功能的属性即bug-prone or not bug-prone
with open(new_fileRoot + projectName_Write + "_sort_semanticmetrics.csv", 'r') as f:
    len_file = len(f.readlines())
classify_file = len_file * 0.1
i = 1
# 标注属性
for key in range(len_file - 1):
    if i <= classify_file:
        df = pd.read_csv(new_fileRoot + projectName + "_sort_codemetrics.csv", encoding='utf-8')
        df['classify'].loc[key] = 'bug-prone'
        df.to_csv(new_fileRoot + projectName + "_sort_codemetrics.csv", encoding='utf-8', index=False)
    else:
        df = pd.read_csv(new_fileRoot + projectName + "_sort_codemetrics.csv", encoding='utf-8')
        df['classify'].loc[key] = 'not bug-prone'
        df.to_csv(new_fileRoot + projectName + "_sort_codemetrics.csv", encoding='utf-8', index=False)
    i += 1
'''
# 3.标注每个功能的属性即bug-prone or not bug-prone bug标准：bugrate大于0，即bug-prone
with open(new_fileRoot + projectName_Write + "_sort_semanticmetrics.csv", 'r') as f:
    len_file = len(f.readlines())
    print(len_file)
df = pd.read_csv(new_fileRoot + projectName_Write + "_sort_semanticmetrics.csv", encoding='utf-8')
for key in range(len_file-1):

    if int(df['Bugrate'].loc[key]) > 0:
        df['classify'].loc[key] ='bug-prone'
        df.to_csv(new_fileRoot + projectName_Write + "_sort_semanticmetrics.csv", encoding='utf-8', index=False)
    else:
        df['classify'].loc[key] = 'not bug-prone'
        df.to_csv(new_fileRoot + projectName_Write + "_sort_semanticmetrics.csv", encoding='utf-8', index=False)

