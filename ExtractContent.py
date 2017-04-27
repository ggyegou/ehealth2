import os
from PreProcess import *
def read(path):
    file_object = open(path,encoding="utf-8")
    state = 0
    topic = ""
    title = ""
    query = ""
    pids = []
    for line in file_object:
        if ("Topic" in line) and (state == 0):
            topic = line.replace("Topic: ","").replace("\n","")
        if ("Title" in line) and (state == 0):
            title = line.replace("Title: ","").replace("\n","")

        if state == 2:
            query += line
        if state == 3:
            pids.append(line.replace("\n","").replace(" ",""))

        if "Query" in line:
            state = 2
        if "Pids" in line:
            state = 3
    return (topic,title,query,pids)
'''
path = "D:\\eHealth\\data of eHealth Task 2\\topics\\"
output = "D:\\eHealth\\data of eHealth Task 2\\topic_processed\\"
for parent,dirnames,filenames in os.walk(path):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字

    for filename in filenames:
        file = path + filename
        print (file)
        (topic,title,query,pids) = read(file)
        query = query_process(query.lower(),"stoplist.txt")
        content = "<top>"
        content += "<topic>"+topic+"</topic>\n"
        content += "<title>"+title+"</title>\n"
        content += "<query>"+query+"</query>\n"
        content += "<pids>\n"
        for pid in pids:
            content+=pid+"\n"
        content += "</pids>\n"
        content+="</top>"
        output_file = open(output+filename,"w+",encoding="utf-8")
        output_file.write(content)
        output_file.close()
'''