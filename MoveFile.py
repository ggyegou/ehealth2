
input_file = open("D:\\eHealth\\data of eHealth Task 2\\qrel_abs_train",encoding="utf-8")


def copy(id):
    origin_file = open("D:\\eHealth\\data of eHealth Task 2\\content_train\\"+id+".txt",encoding="utf-8")
    to = open("D:\\eHealth\\data of eHealth Task 2\\files\\"+id+".txt","w+",encoding="utf-8")
    for line in origin_file:
        to.write(line)
    origin_file.close()
    to.close()


for line in input_file:
    id = line.split(" ")[2]
    copy(id)