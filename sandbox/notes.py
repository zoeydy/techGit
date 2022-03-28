# ###########################
# python 的三种取整方式
# 1.向下取整
int(3.96)
# 2.四舍五入
print(round(3.49),round(3.5))
# 3.向上取整
import math

from numpy import number
math.ceil(2.1)

# ###########################
# set() 去重保持数据位次不变
list1 = [0, 3, 2, 3, 1, 0, 9, 8, 9, 7]
list2 = list(set(list1))
print(list2)        # [0, 1, 2, 3, 7, 8, 9]
list2.sort(key = list1.index)
print(list2)        # [0, 3, 2, 1, 9, 8, 7]
# 反向
round_list = list1[::-1]
list3 = list(set(round_list))
print(list3)
list3.sort(key=round_list.index)
print(list3)


# ###########################
# string -> list
number = 45678
print([int(d) for d in str(number)][::-1])


# ###########################
# list -> string
# 1.comprehension
list1 = [1,2,3,4,5,6]
print(''.join([str(i) for i in list1])) 
print(' '.join(str(i) for i in list1))
# 2.loop
string = ''
for i in list1:
    string += str(i)
print(string)
# 3.all str dtype: just join
output = ['Hello', 'world']
print(' ! '.join(output))
# 4.mix dtype: map()
output = ['Hello', 'world', 1,2,3]
print(' '.join(map(str, output)))
output = ['3', '6', 1,2,3]
print(''.join(map(str,output)))
