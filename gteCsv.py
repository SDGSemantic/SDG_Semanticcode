import os
import understand
import csv

# 提供ubd文件路径，带转换的java文件路径，得到转换的java.csv
def getCsvByfilePath(udb_path,file_path):
    filename = "j"+file_path
    db = understand.open(udb_path)

    file = db.lookup_uniquename(filename)
    result = []
    for lexeme in file.lexer(False, 8, False, True):
        result.append([lexeme.text(), lexeme.token()])
        # print("%s  %s", lexeme.text(), lexeme.token())
    with open(filename[1:] + ".csv", "w", encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(result)

    #if __name__ == '__main__':
      # file_path = "C:\\Users\\sherlock\\project\\avro\\lang\\java\\archetypes\\avro-service-archetype\\src\\main\\resources\\archetype-resources\\src\\main\\java\\service\\SimpleOrderService1.java', 'C:\\Users\\sherlock\\project\\avro\\lang\\java\\archetypes\\avro-service-archetype\\src\\main\\resources\\archetype-resources\\src\\main\\java\\transport\\SimpleOrderServiceClient2.java', 'C:\\Users\\sherlock\\project\\avro\\lang\\java\\archetypes\\avro-service-archetype\\src\\main\\resources\\archetype-resources\\src\\main\\java\\transport\\SimpleOrderServiceEndpoint3.java"
       #udb_path = "C:\\Users\\sherlock\\project\\avro\\avro.udb"
      # getCsvByfilePath(udb_path, file_path)