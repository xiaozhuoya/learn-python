# 迭代器
from collections.abc import Iterator

print(isinstance((x for x in range(10)), Iterator))