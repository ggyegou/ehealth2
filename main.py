from ExtractContent import *

import os.path
import os
from  PreProcess import *
import w2v
path = "D:\\eHealth\\data of eHealth Task 2\\topics\\"
corpus_path = "D:\\eHealth\\data of eHealth Task 2\\processed\\"
output_file = open("D:\\eHealth\\data of eHealth Task 2\\sorted\\result.txt","w+",encoding="utf-8")
w2v.init()
from ListExe import *
for parent,dirnames,filenames in os.walk(path):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字

    for filename in filenames:
        file = path + filename
        print (file)
        (topic,title,query,pids) = read(file)
        query = query_process(query.lower(),"stoplist.txt")
        query_tokens = query.split(" ")
        topic_vec = generateI()
        size1 = 1
        for token in query_tokens:
            try:
                token_vec = w2v.map[token]
                topic_vec = plus(topic_vec, token_vec)
                size1 +=1
            except:
                size1 = size1

        topic_vec = mean(topic_vec,size1)
        #=====================get topic vec finish===============
        scores = dict()
        for pid in pids:
            content = ""
            abs_vec = generateI()
            size2 = 1
            try:
                _file = open(corpus_path+pid+".txt",encoding="utf-8")
                for line in _file:
                    content += line
                title = content[content.index("<title>"):content.index("</title>")].replace("<title>", "").replace("\n", "")
                abs = content[content.index("<abstract>"):content.index("</abstract>")].replace("<abstract>", "").replace("\n","")
                title_tokens = title.split(" ")
                abs_tokens = abs.split(" ")

                for token in abs_tokens:
                    try:
                        token_vec = w2v.map[token]
                        abs_vec = plus(abs_vec,token_vec)
                        size2 += 1
                    except:
                        size2 = size2
                abs_vec = mean(abs_vec, size2)
            except:
                abs_vec = generateI()

            #=============get pid's vec finished===============
            score = cosvalue(topic_vec,abs_vec)
            scores[pid] = score
        res = sorted(scores.items(), key=lambda item: item[1], reverse=True)
        for i in range(0,len(res)):
            pair = res[i]
            output_file.write(topic+" TBD " + pair[0] + " "+str(i+1) +" "+str(pair[1])+" "+"1\n")
output_file.close()