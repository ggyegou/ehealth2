import re
def clear(content,stop,biaodian):
    _content = content
    for item in biaodian:
        _content = _content.replace(item," ")
    _content, num1 = re.subn("\s+", " ", _content)
    _content_w = _content.split(" ")
    _result = []
    result = ""
    for item in _content_w:
        tag = 1
        for word in stop:
            if word == item:
                tag = 0
                break
        if tag == 1:
            _result.append(item)
    for item in _result:
        result += item + " "
    return result
def corpus(_content,stop,biaodian):
    content = str(_content)
    title = content[content.index("<title>"):content.index("</title>")].replace("<title>","").replace("\n","")
    abs = content[content.index("<abstract>"):content.index("</abstract>")].replace("<abstract>","").replace("\n","")
    title = clear(title,stop,biaodian)
    abs = clear(abs,stop,biaodian)
    return (title,abs)

def query_process(query,stoplist):
    file = open(stoplist)
    file2 = open("biaodian.txt",encoding="utf-8")
    for line in file2:
        query = query.replace(line.replace("\n",""),"")
    query,num = re.subn("\s+", " ", query)
    for line in file:
        word = line.replace("\n","")
        query = query.replace(word,"")
    _query,number = re.subn("\s+"," ",query.lower())
    _query = _query.replace("\n","")
    return _query