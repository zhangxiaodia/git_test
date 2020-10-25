import json

s = {"test1":1,"test2":2}
json_d =json.dumps(s)
json_l =json.loads(json_d)

print("json_d的值为{},其类型是{}".format(json_d, type(json_d)))
print("json_d的值为{},其类型是{}".format(json_l, type(json_l)))

