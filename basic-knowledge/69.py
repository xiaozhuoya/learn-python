# 操作文件和目录

import os
os.name
# os.uname()

# 操作系统中定义的环境变量
os.environ
# 当前文件绝对路径
os.path.abspath('.') 

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
os.path.join('/Users/michael', 'testdir')
# 然后创建一个目录:
os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
os.rmdir('/Users/michael/testdir')

