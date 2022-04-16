
############### sort numbers ###############
# tst = [3,19,0,2,7]
# # tst
# # sorted(tst, reverse=True)

# def sort(li):
#     print(sorted(li, reverse = True))

############### test ###############


# import numpy as np

# test_array = np.arange(25)+1
# test_matrix = np.asmatrix(test_array)
# print(test_matrix)
# # test = np.matrix(range(5),range(6,10),range(11,15),range(16,20),range(21,25))
# # print(test)
# # test_rev = test[::-1]
# # print(test_rev)



########################
from ast import Break
from curses import ACS_DARROW
from imghdr import tests
import imp
import sys
from time import time
from traceback import print_tb
from turtle import st
from unittest import result, skip
from pyparsing import restOfLine
from pyrsistent import T
from sklearn import impute

from sympy import li, ordered, re, separatevars, sring

from techGit.py_turing.function import add 
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        for v in values:
            ans += v
    print(ans)



import numpy as np
 
a = [1,2,3,4,5,6,7,7]

import sys
inpu = sys.stdin.readline().strip()
inpu = list(inpu)

for i in range(len(inpu)):
    times = 1
    while i < len(inpu):
        if inpu[i-1] == inpu[i]:
            times += 1
            inpu.remove(inpu[i])
        elif times == 1:
            pass
        else:
            inpu.insert(i, times)


    print(' '.join(str(e) for e in inpu))


# ######################################################
# """ 兴业数金笔试题：输入字符串，每个数字后跟‘，’， 组成一个数字+1，返回每个数位的数字后跟‘，’ """
# import sys

# def str2num(inpu):
#     res = []
#     for i in inpu: 
#         if i == ",":
#            continue
#         else:
#             res.append(i)
#     return res


# inpu = sys.stdin.readline().strip()
# num = ''.join(str2num(inpu))

# if num[0] == "0":
#     print("请输入以非0开头的数字")
#     sys.exit()

# if inpu.count(',') + 1 < len(num):
#     print("请在每个位数输入一位数字")
#     sys.exit()

# num = int(num)
# add1 = num + 1
# outpu = str(add1)
# print(','.join(outpu), end=",")
# ######################################################


# ######################################################
# """ 兴业数金笔试题：输入一个5位数，最多两个0，0可以代替任何数字
#     如果能输出排序数组则成功 e.g. 23456 否则失败 """
# import sys
# inpu = sys.stdin.readline()
# num = list(inpu)[:-1]

# # 1. check whether the number of 0 is bigger than 2
# if sorted(num)[2] == '0':
#     print("the maximum number of '0's is 2")
# elif len(num) != 5:
#     # 2. check whether the length of the sring equals 5
#     print("the length of the string is required to be 5")
# else:
#     # 3. main
#     dele0 = [i for i in num if i != '0']
#     first = int(sorted(dele0)[0])
#     dele0.remove(str(first))
#     temp = first
#     round = 5

#     while round > 1:

#         if str(temp + 1) in dele0:
#             dele0.remove(str(temp + 1))
#             temp += 1
#             round -= 1
#         elif '0' in num:
#             num.remove('0')
#             temp += 1
#             round -= 1
#         else:
#             print("oh my god!")
#             break
    
#     if round == 1:
#         print("so lucky!")
# ######################################################


# ######################################################
# 牛客华为 笔试题 regular expression
# https://www.nowcoder.com/practice/119bcca3befb405fbe58abe9c532eb29?tpId=37&tqId=21240&rp=1&ru=/ta/huawei&qru=/ta/huawei&difficulty=3&judgeStatus=&tags=/question-ranking
# import sys
# import re

# inpu = sys.stdin.readline()
# strin = inpu.split(sep = ';')

# if len(strin) > 10000 | len(strin) < 1:
#     sys.stdout("字符串长度需要在1到10000间")
# 
# def match_pattern(my_string):
#     match = re.search(r'[ASDW]\d+$', my_string)
#     if match:
#         return match.group()
#     else:
#         next

# def main(strin):
#     originX = 0
#     originY = 0 

#     for i in strin:
#         if len(i) > 3:
#             continue
#         else:
#             coordinate = match_pattern(i)
#             # print(coordinate)
        
#         if coordinate:
#             if coordinate[0]== 'A':
#                 originX = originX - int(coordinate[1:])
#             elif coordinate[0]== 'D':
#                 originX = originX + int(coordinate[1:])
#             elif coordinate[0]== 'W':
#                 originY = originY + int(coordinate[1:])
#             elif coordinate[0]== 'S':
#                 originY = originY - int(coordinate[1:])
#         else:
#             continue

#     return originX,originY
        
    
# result = main(strin)

# print(f'{result[0]},{result[1]}')

# ######################################################
    

# ######################################################
# 牛客华为 笔试题 regular expression
# https://www.nowcoder.com/practice/8c949ea5f36f422594b306a2300315da?tpId=37&tqId=21224&rp=1&ru=/ta/huawei&qru=/ta/huawei&difficulty=&judgeStatus=&tags=/question-ranking

# import sys
# import re

# inpu = sys.stdin.readline()

# if len(inpu) <= 1:
#     sys.stdout('Please input the string')
#     sys.exit()
    
# if len(inpu) > 5000:
#     sys.stdout("The length of the string is required to be less than 5000")
#     sys.exit()
    

# if re.search(r'\s\w+$', inpu):
#     word = re.search(r'\s\w+$', inpu)
#     result = len(word.group())-1
#     sys.stdout.write(str(result))
# elif re.search(r'\s?\w+$', inpu):
#     word = re.search(r'\s?\w+$', inpu)
#     result = len(word.group())
#     sys.stdout.write(str(result))
# else:
#     sys.exit()
# ######################################################


# # huawei weitijiao
# import re

# size = int(input())
# array = input()
# order = int(input())

# sep_array = array.split(sep=' ')

# list = [int(i) for i in sep_array]


# if order == 0: 
#     print(sorted(list))
# else:
#     print(sorted(list)[::-1])

students = [[3,'Jack',12],[2,'Rose',13],[1,'Tom',10],[5,'Sam',12],[4,'Joy',8]]
#按学号顺序排序：
sorted(students,key=(lambda x:x[0]))
#结果
[[1, 'Tom', 10], [2, 'Rose', 13], [3, 'Jack', 12], [4, 'Joy', 8], [5, 'Sam', 12]]
 
#按照名字排序
sorted(students,key=(lambda x:x[1]))
[[3, 'Jack', 12], [4, 'Joy', 8], [2, 'Rose', 13], [5, 'Sam', 12], [1, 'Tom', 10]]
 
#按年龄倒序排序：
sorted(students,key=(lambda x:x[2]),reverse=True)
[[2, 'Rose', 13], [3, 'Jack', 12], [5, 'Sam', 12], [1, 'Tom', 10], [4, 'Joy', 8]]
 
#按年龄为主要关键字，名字为次要关键字倒序排序：
sorted(students,key=(lambda x:[x[2],x[1]]),reverse=True)
[[2, 'Rose', 13], [5, 'Sam', 12], [3, 'Jack', 12], [1, 'Tom', 10], [4, 'Joy', 8]]