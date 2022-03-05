
from optparse import OptParseError


f1 = open('turingPython/test.txt', 'rt') # 默认‘rt’模式：读 文本
print(f1.read())
f1.close()

f2 = open('turingPython/test.txt', 'rt') # 默认‘rt’模式：读 文本
print(f2.read(10)) # 返回特定个数个字符
f2.close()

# readline
f3 = open('turingPython/test.txt', 'rt') # 默认‘rt’模式：读 文本
print(f3.readline())
print(f3.readline())
print(f3.readline())
f3.close()

f4 = open('turingPython/test.txt', 'rt') # 默认‘rt’模式：读 文本
for i in f4:
    print(i)
f4.close()


