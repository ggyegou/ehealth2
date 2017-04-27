map = dict()
map["1"] = 5
map["2"] = 3
map["3"] =7

res = sorted(map.items(),key=lambda item:item[1],reverse=True)

print (res)