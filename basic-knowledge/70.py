# 序列化
import pickle
d = dict(name='Bob',age = 20,score = 88)

pickle.dumps(d)

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()