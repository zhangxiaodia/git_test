import pickle

'''
pickle对象序列化工具，对于内存中几乎所有类型的对象，都能将其转化成字符串，凭借此字符串，可通过此字符串重建为最初的对象，主要有以下作用：
1. 持久化
2. 程序间通讯
'''
s = 'demi'
pickle_d = pickle.dumps(s)
pickle_d2 = pickle.dumps(s)
pickle_l = pickle.loads(pickle_d)

print("pickle_d的值为%s,%s" % (pickle_d, type(pickle_d)))
print("pickle_d的值为%s,%s" % (pickle_d2, type(pickle_d2)))
print("pickle_l的值为%s,%s" % (pickle_l, type(pickle_l)))
