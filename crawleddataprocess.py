import os.path
import os
from PreProcess import *
path = "D:\\eHealth\\data of eHealth Task 2\\files\\"
outputpath = "D:\\eHealth\\data of eHealth Task 2\\processed\\"
stop = []
stop_file = open("corpus_stop.txt",encoding="utf-8")
for line in stop_file:
    stop.append(line.replace(" ","").replace("\n",""))
biaodian = []
biaodian_file = open("biaodian.txt",encoding="utf-8")
for line in biaodian_file:
    biaodian.append(line.replace(" ","").replace("\n",""))
print(biaodian)
def execute(filename):

    output = open(outputpath+filename,"w+",encoding="utf-8")
    content = ""
    try:
        file = open(path + filename, encoding="utf-8")
        for line in file:
            content += line
        title,abs = corpus(content.lower(), stop, biaodian)
    except:
        title =""
        abs = ""
    output.write("<DOC><DOCNO>"+filename.replace(".txt","")+"</DOCNO>")
    output.write("<title>"+title+"</title>\n")
    output.write("<abstract>" + abs + "</abstract>\n")
    output.write("</DOC>")
    output.close()
for parent,dirnames,filenames in os.walk(path):    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字

    for filename in filenames:
        print("doing: "+filename)
        execute(filename)


