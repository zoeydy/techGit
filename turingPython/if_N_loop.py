

# if statement
from email import message
from lib2to3.pgen2.token import LBRACE
from msilib.schema import ListBox
from pickle import TRUE
from platform import libc_ver
from click import style
from sqlalchemy import false, true
from sympy import re


age = 20
adult = False
if age >= 18:
    adult = True
print(adult) 

iftest = ['a', 'd', 'e', 't', 'y']
if 'a' in iftest:
    for letter in iftest:
        print(letter.upper())
        
height = 180
result = "tall" if height > 170 else "short"
result




# while loop
# # break & continue
# enter quit to exit
prompt = "enter quit to end the program \n"
message = ""
while message.lower() != "quit":
    message = input(prompt)
    print(message)

exi = True
while exi:
    message = input(prompt)
    if message.lower() == 'quit':
        exi = False
    else:
        print("you need to type in 'quit' to end the program")
# use 'break' to make it easier
message = input(prompt)
while True:
    if message.lower() == "quit":
        break
    else:
        message = input(prompt)
# use continue to skip the afterward steps in the loop
# # e.g. skip the even num
num = 0
while num < 11:
    num += 1
    if num%2 == 0:
        continue
    else:
        print(num)

# 在数组list和dictionary里使用while语句
friends = []
prompt = "Enter your friend's name: "
while True:
    friend = input(prompt)
    if friend == 'q':
        break
    friends.append(friend)
print(friends)

listA = ['a', 'b', 'd', 'c', 'l']
ListB = []
while listA:
    ListB.append(listA.pop())
print(listA)
print(ListB)
while 'a' in ListB:
    ListB.remove('a')

# for loop
listLoop = range(3,9)
for num in listLoop:
    print(num)

for i in range(1,30,3):
    print(i)

# exercise: 在一个永久循环中，提示用户输入两个数字，并答应两个数字间的所有奇数，如1，5则输出1，3，5
# 如果用户输入第一个数字大于第二个数字结束循环
while True:
    res = input("Please enter 2 numbers: ")
    head = int(res[0])
    tail = int(res[2])
    if head > tail:
        break 
    else:
        output = []
        for i in range(head, tail+1):
            if i%2 == 1:
                output.append(i)
        print(output)
