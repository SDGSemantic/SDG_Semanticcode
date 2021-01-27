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

def getls(allfile,comparing_file_name):
    # logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    # 需要进行比较的文件名
    # comparing_file_name = 'C:\\Users\\wsz\\Desktop\\Group\\apache_project_codeAndMetric\\source_code\\ant\\src\\main\\org\\apache\\tools\\mail\\MailMessage.java'
    # 保存所有被编号的独一无二的文件名的文件
    file_names_numbering = allfile
    # 基准相似距离
    base_similarity_distance =0.8

    # 打开包含所有文件名的目录
    with open(file_names_numbering, 'r') as all_names_file:
        # 读取文件内容
        topic_filename = csv.reader(all_names_file)
        # 去除停用词，得到有用的信息文本
        documents = []
        query_target = ''
        for file_line in topic_filename:
            if file_line == '':
                break
            try:
                file_name = open(file_line[0] + ".csv", 'r', encoding='utf-8')
            except FileNotFoundError as e:
                print("文件找不到", e)
                continue

            # 读取文件内容
            file_content = csv.reader(file_name)
            file_to_str = ""
            clear_flag = -2
            for content in file_content:
                if clear_flag < 0:
                    clear_flag += 1
                    continue
                if (content[1] == "Comment" or content[1] == "Identifier"):
                    file_to_str += " " + content[0]

            file_to_str = file_to_str.lower()
            text_list = re.sub("[^a-zA-Z]", " ", file_to_str).split()

            # 2 q去掉标点符号和停用词
            # 去掉标点符号
            english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%', '"', '//*',
                                    '*//']
            text_list = [word for word in text_list if word not in english_punctuations]
            # 去掉停用词
            stops = set(stopwords.words("english"))
            text_list = [word for word in text_list if word not in stops]
            str_text = ""
            for list in text_list:
                str_text += ' ' + list
            # print(str(file_line[0]),comparing_file_name)
            if file_line[0] == comparing_file_name:
                query_target = str_text
            documents.append(str_text)
            file_name.close()
    texts = [[word for word in document.lower().split()] for document in documents]
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=50)
    corpus_lsi = lsi[corpus_tfidf]
    index = similarities.MatrixSimilarity(lsi[corpus])
    query = query_target
    query_bow = dictionary.doc2bow(query.lower().split())

    query_lsi = lsi[query_bow]
    returnList=[]
    sims = index[query_lsi]
    similiar_file_count = 0
    file_Sum_count=0
    distance_sum = 0
    for distance in sims:
        distance_Sum+=distance
        file_Sum_count+=1
        if distance >= base_similarity_distance:
            distance_sum += distance
        similiar_file_count += distance >= base_similarity_distance

    similiar_file_count -= 1
    if similiar_file_count == 0:
        #similiar_file_count = 1
        distance_sum = 0

    sort_sims = sorted(enumerate(sims), key=lambda item: -item[1])
    # print("All file number is %d" % len(sort_sims))
    returnList.append(distance_sum)
    returnList.append((similiar_file_count,distance_Sum,file_Sum_count))
    return returnList