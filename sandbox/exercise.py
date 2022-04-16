

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
