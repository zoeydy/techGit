

import enum
import sys
from tkinter.font import names

from matplotlib.pyplot import cla
print(sys.stderr)

# stdin input
print(
    'get string answer: '
)
test1 = sys.stdin.readline()

print(
    'get integer: '
)
test2 = int(sys.stdin.readline())

print(
    'get numbers: '
)
test3 = int(sys.stdin.readline().strip('\n'))

print(
    'input several numbers: '
)
test4 = sys.stdin.readline().strip('')
test5 = list(map(int, test4.split())) # change the string into list

# sys
sys.stdout.write("the length of the string: ")
sys.platform
sys.version

# 实用函数
dir
dir() # 全局变量
dir(sys) # sys中包含的变量 即：显示对象的属性

# help()
int()
float()
len({1:2,3:4})

# open()
range(0,3)
str()
type(type((1,2,3,4,5)))

class A:
    def __str__(self):
        print(
            'this is a string'
        )

a = A()
a.__str__()





# 抑制换行符
for i in 'hello':
    print(i)
for i in 'hello':
    print(i, end = '')
for i in 'hello':
    print(i, end = '!')
for i in 'hello':
    print(i, end = '\n\n')

# docstring
three_quo = """ test
it
! """
print(three_quo)

# 列表解析
print([a for a in 'hello'])

num = [1,2,3,4,5,6,7]
odd = [i for i in num if i%2]
print(odd)

cube = [x**3 for x in range(0,5)]
print(cube)
even = [i for i in cube if not i%2]
even

dic = {'one':1, 'two':2, 'three':3}
dic_cube = {key+"_cube": value**3 for key, value in dic.items()}
dic_cube

# enumerate
names = ['alex', 'elin', 'cole', 'matt']
for inde, name in enumerate(names):
    print(inde, name)

# for & else
for i in range(0,10):
    if i == 12:
        print('found')
else:
    print('not found')