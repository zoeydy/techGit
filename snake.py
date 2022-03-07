

from posixpath import split
import pprint
import numpy as np


N, M = eval(input('请输入矩阵大小及你要查询的数字：'))


def trans90(matrix):
    matrix = matrix[::-1]   #先反转
    rows,cols = len(matrix),len(matrix[0])
    for i in range(rows):   #做转置，对角线不交换，把右上三角换到左下三角
        for j in range(i,cols):   #注意从i开始，不要换了又把左下三角换回去了
            if i==j:
                continue
            else:
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    return matrix
 
def snake():
    
    myarray = np.zeros((N, N), dtype=np.int16)
    x, y = 0, 0
    res = myarray[x][y] = 1
    while(res < N * N):
        while(x + 1 < N and (not myarray[x + 1][y])):
            res += 1
            x += 1
            myarray[x][y] = res
        while(y - 1 >= 0 and not myarray[x][y - 1]):
            res += 1
            y -= 1
            myarray[x][y] = res
        while(x - 1 >= 0 and not myarray[x - 1][y]):
            res += 1
            x -= 1
            myarray[x][y] = res
        while(y + 1 < N and not myarray[x][y + 1]):
            res += 1
            y += 1
            myarray[x][y] = res
 
    print(np.asmatrix(myarray))
    return(np.asmatrix(myarray))


def main():
    print(trans90(snake()))
    itemindex = np.argwhere(trans90(snake()) == M) + 1
    print (itemindex)
 
if __name__ == '__main__':
    main()
