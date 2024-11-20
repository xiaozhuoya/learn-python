# sorted
S = sorted([36, 5, -12, 9, -21])
print(S)

S1 = sorted([36, 5, -12, 9, -21],key=abs)
print(S1)

# 小写
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
# 反转
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
