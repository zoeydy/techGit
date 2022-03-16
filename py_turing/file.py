from codecs import namereplace_errors
from distutils.log import error
import os
from re import X
from shutil import which
from sys import path



f1 = open('test.txt', 'rt') # 默认‘rt’模式：读 文本
print(f1.read())
f1.close()

f2 = open('test.txt', 'rt') # 默认‘rt’模式：读 文本
print(f2.read(10)) # 返回特定个数个字符
f2.close()

# readline
f3 = open('test.txt', 'rt') # 默认‘rt’模式：读 文本
print(f3.readline())
print(f3.readline())
print(f3.readline())
f3.close()


f5 = open("test.txt", "a")
f5.write("\nthis is the new content.")
f5.close()

f4 = open('test.txt', 'rt') # 默认‘rt’模式：读 文本
for i in f4:
    print(i)
f4.close()

# 创建文件 “a” ‘x'
f = open('a_txt.txt', "a")
f = open("w_txt.txt", "w")

if os.path.exists('x_txt.txt'):
    os.remove('x_txt.txt') # 没有文件存在会报错
else:
    f = open('x_txt.txt', "x") # 若文件已存在会报错

# os.rmdir("your_directory")

with open("test.txt") as f:
    print(f.read())


# error deal
# try()

try:
    f = open('test.txt')
    f.write("something")

    print(noth)

except NameError:
    print("1st try: variable noth is not defined")
except:
    print('1st try: something wrong happend when writing file')

finally:
    f.close()


try:
    print(noth)

    f = open('test.txt')
    f.write("something")  

except NameError:
    print("2ed try: variable noth is not defined")
except:
    print('2ed try: something wrong happend when writing file')
    
finally:
    f.close()


# exercise




# if os.path.exists(file_name):

def file_operator(file_name, mode):
    try:
        if mode.lower() == "w":
            with open(file_name, "a") as f:
                f.write("\nThis is the new content.")
                f.close()
            with open(file_name) as f:
                f.read()
                f.close()
        else:
            with open(file_name) as f:
                print(f.read())
                f.close()

    except NameError:
        print("name error")

    except:
        print(f'There is no file named {file_name}')


def main():
    file_name = input('Which file do you want to operate? ')
    mode = input("do you want to read(r) or write(w) the file? ")
    file_operator(file_name, mode)
    
if __name__ == '__main__':
    main()

