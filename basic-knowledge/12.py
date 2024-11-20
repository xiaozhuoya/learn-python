# set 无重复元素的集合
s = {1, 2, 3}
print(s)
s = set([1, 2, 3])
print(s)
s = {1, 1, 2, 2, 3, 3}
print(s)
s.add(5)
s.remove(2)