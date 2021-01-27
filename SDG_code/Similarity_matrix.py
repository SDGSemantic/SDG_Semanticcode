# 算出相似矩阵
from gensim import corpora, models, similarities
import logging
import csv
import re
from nltk.corpus import stopwords
from getCsv import getCsvByfilePath
from getls import getls
#注：无base_similarity_distance
def Similarrity_Matrix(Write_path,readString,file_list):

    for comparing_file_name in file_list:
        resultStr = getls(readString, comparing_file_name)
        f = open(Write_path+'_matrix_reflection.txt', 'a')
        f.write(resultStr + '\n')
        f.close()

