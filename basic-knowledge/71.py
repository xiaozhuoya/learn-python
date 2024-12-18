# JSON

import json
d = dict(name = 'Bob',age = 20,score = 88)
json.dumps(d)
print(json.dumps(d))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'

print(json.loads(json_str))


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
print(json.dumps(s))

