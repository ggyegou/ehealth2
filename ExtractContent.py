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
