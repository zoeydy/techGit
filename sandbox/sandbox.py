
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
import sys
from time import time
from pyrsistent import T

from sympy import li 
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