# StringIO和BytesIO

from io import StringIO,BytesIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

f1 = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f1.readline()
    if s == '':
        break
    print(s.strip())


# BytesIO
f2 = BytesIO()
f2.write('中文'.encode('utf-8'))
print(f2.getvalue())

f3 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')

print(f3.read())
