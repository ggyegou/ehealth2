from ListExe import *
from ExtractContent import *
from PreProcess import *
file = open("D:\\eHealth\\data of eHealth Task 2\\glove.840B.300d.txt",encoding="utf-8")
map = dict()
vocabulary = []

def init():
    getVocabulary()
    for line in file:
        tokens = line.split(" ")
        word = tokens[0]
        if(word in vocabulary):
            map[word] = []
            for i in range(1,301):
                map[word].append(float(tokens[i]))
        del tokens
    print ("init finish",len(map))

def init2():
    map["a"] = generateZero()
    map["the"] =generateZero()
    print ("inti2")

def getVocabulary():
    path = "D:\\eHealth\\data of eHealth Task 2\\topics\\"
    corpus_path = "D:\\eHealth\\data of eHealth Task 2\\processed\\"
    for parent, dirnames, filenames in os.walk(path):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字

        for filename in filenames:
            file = path + filename
            print(file)
            (topic, title, query, pids) = read(file)
            query = query_process(query.lower(), "stoplist.txt")
            query_tokens = query.split(" ")
            title_tokens = title.split(" ")
            for item in query_tokens:
                if item not in vocabulary:
                    vocabulary.append(item)
            for item in title_tokens:
                if item not in vocabulary:
                    vocabulary.append(item)
    for parent, dirnames, filenames in os.walk(corpus_path):
        for filename in filenames:
            _file = open(corpus_path + filename, encoding="utf-8")
            content = ""
            for line in _file:
                content += line
            title = content[content.index("<title>"):content.index("</title>")].replace("<title>", "").replace("\n", "")
            abs = content[content.index("<abstract>"):content.index("</abstract>")].replace("<abstract>", "").replace("\n", "")
            title_tokens = title.split(" ")
            abs_tokens = abs.split(" ")
            for item in abs_tokens:
                if item not in vocabulary:
                    vocabulary.append(item)
            for item in title_tokens:
                if item not in vocabulary:
                    vocabulary.append(item)
    print (vocabulary[0:10])
    print (len(vocabulary))
#getVocabulary()