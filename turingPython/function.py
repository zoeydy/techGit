


from ast import expr
from audioop import lin2adpcm
import readline
from tkinter import W

from numpy import array
from sympy import li


def add(num1, num2):
    print(f"The sum is {num1 + num2}")

add(2,3)

def expre():
    age = input("How old are you? ")
    name = input("What is your name? ")
    print(f"Hello, {name}, You are {age} years old.")

expre()

# 加入key word就可以不管变量输入顺序
def isbiger(a,b):
    if a < b:
        print(f"{a} is not bigger than {b}")
    else:
        print(f"{a} is bigger than {b}")

isbiger(b = 3, a = 6)

# default values
def defva(val = "default value"):
    print(f"This is the {val}")

defva("input value")

testList = ['a', 'b', 'c', 'd']
def readList(inpuList):
    for i in inpuList:
        print(i)
readList(testList)

# 不影响原数据做操作
numList = [1,2,3,4,5]
def setToOne(inpuList):
    for i in range(0,len(inpuList)):
        inpuList[i] = 1
setToOne(numList)
numList
numList = [1,2,3,4,5]
setToOne(numList[:])
numList

# variadic function 可变参数 参数数量不定
def report(name, *grades): # 可变参数一定要在正常参数之后
    totalGrade = 0
    for grade in grades:
        totalGrade += grade
    print(f"The total grade for {name} is {totalGrade}")

report("zoey", 100,99,100)

# 关键字参数
# 在函数内部，这些参数会被封装成dictionary
def info(name, **kw):
    print(f"{name}'s information is: ")
    for k, w in kw.items():
        print(f"{k}: {w}")

info("zoey", height = 169, education = "master", hobby = "Music")

# return value
def formatName(firstName, lastName):
    return f"The formatted name is {firstName} {lastName}"

formatName("zoey", "dy")


def change2Dic(var1, var2):
    return {"first variable": var1, "second variable": var2}
res = change2Dic("a", "b")  
type(res)



# 局部/全局 variable (CMEE更好)
# import (CMEE更好)


# recursion function
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

fact(5)


# ? lambda function 没有具体名称，可以有多个变量，但是只有一个表达式
# 简洁的实现一次性小功能
def myFun(n):
    return lambda a: a*n
myTrip = myFun(3)
myTrip(5)

# ? 程序入口判断
# if __name == '__main__':
    # statement



# exercise
def sumList(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    if len1 > len2:
        temp = list2
        list2 = list1
        list1 = temp

        templ = len2
        len2 = len1
        len1 = templ

    resList = []
    for i in range(0, len1):
        resList.append(list1[i] + list2[i])
    resList = resList + list2[len1:len2]
    return resList

sumList([1,2,3,5,3], [2,3,4])