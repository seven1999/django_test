# -*- coding: utf-8 -*-

# @Time    : 2019/6/9 19:45
# @Author  : Administrator
# @Comment : 清楚pyc文件        https://www.cnblogs.com/love9527/p/8036867.html


import os

path = 'E:\\frontend\\dj_backend'                # project-path
print(os.walk(path))

for prefix, dirs, files in os.walk(path):
    for name in files:
        if name.endswith('.pyc'):
            filename = os.path.join(prefix, name)
            os.remove(filename)


