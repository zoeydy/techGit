

""" 1.
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择某一天买入这只股票，并选择在未来的某一个不同的日子卖出该股票。

设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。 """


from difflib import restore


class Solution1:
    def maxProfit(self, prices):
        min_price= int(1e9)
        max_profit = 0
        for price in prices:
            max_profit = max(price - min_price, max_profit)
            min_price = min(price, min_price)
        return max_profit

max_pri = Solution1()
max_pri.maxProfit([7,1,5,3,6,4])
max_pri.maxProfit([7,6,4,3,1])

""" 2.
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
"""
class FibonacciVar:
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007

fib = FibonacciVar()
fib.numWays(7)



""" 3.计算某字符出现的次数 """

array = input()
obj = input()

array = str(array.lower())
obj = obj.lower()

num = 0
for i in range(len(array)):

    if array[i] == obj:
        num += 1
    else:
        next

print(num)



""" 4.N+随机数，返回不重复数字 """
N = input()
N = int(N)

list = []
for i in range(N):
    temp = input()
    temp = int(temp)
    list.append(temp)

result = set(list)
result = sorted(result)

for j in result:
    print(j)


""" 5.字符串分割 """

string = input()

def separate(string):
    groups = int(len(string) / 8)
    for i in range(groups):
        print(string[i*8:(i+1)*8])

if len(string) % 8 == 0:
    separate(string)
else:
    add = 8-len(string) % 8
    add_0 = '0'*add
    string = string + add_0
    separate(string)



""" 6. 计算成绩(最少学习时间) """
import numpy as np
import sys
import re

# define the functions
def match_num(inpu):
    match = re.findall(r'\d+\s?',inpu)
    return match

# read the data
inpu = sys.stdin.readlines()
data = [[0 for i in range(3)] for j in range(len(inpu))]
for i in range(len(inpu)):
    size = len(match_num(inpu[i]))
    temp = []
    for j in range(size):
        temp.append(int(match_num(inpu[i])[j]))
        data[i] = temp

# define main
# 1.有几组数据需要处理

rest = data
heads = [i for i in data if len(i) == 3]
for i in range(len(heads)):
    n = heads[i][0]
    r = heads[i][1]
    avg = heads[i][2]
    group = rest[0:n+1]
    rest = rest[n+1:]
    # calculatation
    min_score = 0
    b_list = []
    for j in range(n):
        min_score += group[j+1][0]
        if int(group[j+1][1]) in b_list:
            next
        else:
            b_list.append(int(group[j+1][1]))

    # 判断分数
    if min_score >= n*avg:
        print(0)
    else:
        lower = min_score
        upper = min_score
        t = 0
        # 需要处理几个b值
        times = 0
        while upper < n*avg:
            
            b_loop = sorted(b_list)[times]
            
            for l in range(n):
                a = group[l+1][0]
                b = group[l+1][1]
                if b == b_loop:
                    upper += (r-a) 
                else:
                    next 
                    
            t += (upper-lower)*b_loop
            lower = upper 
            times += 1
        print(t+((n*avg-lower)*b_loop))


# ##################################
# # 用numpy
# inpu = input()
# if len(match_num(inpu)) == 3:

#     n = int(match_num(inpu)[0])
#     r = int(match_num(inpu)[1])
#     avg = int(match_num(inpu)[2])

#     table = np.zeros((n,2))
#     for i in range(n):
#         inpu = input()
#         table[i,0] = int(match_num(inpu)[0])
#         table[i,1] = int(match_num(inpu)[1])

#     min_score = np.sum(table, axis=0)[0]
#     if min_score >= n*avg:
#         print(0)
#     else:
#         loop_time = len(set(np.sort(table[:,1])))
#         upper = min_score

#         for j in range(loop_time):
#             min_b = list(set(np.sort(table[:,1])))[j]
#             lower = upper
#             upper = 0
#             for k in range(n):
#                 if table[k,1] == min_b:
#                     upper += r
#                 else:
#                     upper += table[k,0]
        
#                 if upper >= n*avg:
#                     print((n*avg-min_score)*min_b)
#                     exit

