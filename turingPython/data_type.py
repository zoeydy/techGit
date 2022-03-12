

name = input("what's your name?")
print("hello, ", name)

a = 1
b = 1
print(id(a) == id(b))

string = "Hello"
print(string.isalnum())
print(string.isalpha())
print(string.isupper())

a, b, c, d = True, 3, 3.3, 3+3
print(type(a),type(b),type(c),type(d))

3*0.1
14_000_000_000

print('This is why you need two kinds of "quotation marks"')
firstName = "zoey "
lastName = "dy"
fullName = f"{firstName}{lastName}"
print(firstName + lastName[0])
print(fullName)
print(firstName.upper())
print(firstName.upper().lower())
print(fullName.title())

# special charector
print("This is the special mark \'")
print("when you want to type the backslash", r'\ ') # you need a space after \

# format 
# 1
message = "{} was born in {}"
print(message.format('Python', 1991))
# 2
print("%s was born in %d." %('Python', 1991))
# 3
name = "Python"
year = 1991
print(f"{name} was born in {year}.")


# Python 变量和基础数据类型
# 序列数据类型 list tuple dictionary set

# List 可修改数据类型 包括自定义数据类型 [xxx, xx, xxx, ...] 方括号➕逗号
letters = ['a', 'b', 'c', 'm', 'h', 'y']
print(letters[2:5]) #下闭上开
letters[5] = 'change'
print(letters)
letters[-2] = "- test"
print(letters)
if 'a' in letters:
    print('letter a is in the list letters')

## list 的运算
listTest = ['apple', 'pinapple']
listTest.insert(1, "index 1") # insert
print(listTest)
listTest.remove('apple') # remove
print(listTest)
list2 = listTest.copy() # copy
print(list2)
list2.append("append") # append
print(list2)
del list2[0] # delete
print(list2)
list2.clear() # clear

print(list2 + listTest)
print(list2 * 3)
print(sorted(letters)) # sorted
print(letters)
letters.sort() #.sort()
print(letters)
letters.reverse() # reverse
print(letters)


## tuple 元素创建后不能被修改
tupleTest = (300, 333)
tupleTest
## 另外赋值的方法 tupleTest[0] = X is not gonna work
tupleTest = (100, 100) # 但可以全部修改
tupleTest
## 遍历tuple里的元素
for num in tupleTest:
    print(num)
## comprehension
f = [num for num in tupleTest]
print(f)


## 内置函数
len(letters)
nums = [2,5,33,1,0,-3]
min(nums)
max(nums)


# Dictionary
student1 = {'gender': 'male', 'age': 18}
print(student1['gender'])
print(student1['age'])
## add new key
student1[0] = 'female'
student1['grade'] = 100
student1['name'] = 'Daniel'
student1
## dictionary的其他运算
del student1['name'] # delete element
student1
student1.clear() # clear
student1
del student1 # delete the whole
## 遍历 dictionary
student1 = {'gender': 'male', 'age': "18"}
student1.get('gender')
student1.keys()
student1.items()

for key, value in student1.items():
    print(f"\nkey: {key}")
    print(f"Value: {value}")
for key in student1.keys():
    print(key + ": " + student1.get(key))
for key in sorted(student1.keys()):
    print(key)
    print(key.title())
## format output
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
print(f"You ordered a {pizza['crust']} pizza, with the following toppings: {pizza['toppings']}")
for topping in pizza['toppings']:
    print("\t" + topping) # \t 制表符

## 嵌套 nesting, a dictionary in dictionary
users = {
    'Enoch': {
        'fullName': 'xiao wang',
        'age': 25
    },
    'Fandy': {
        'fullName': 'wang hong',
        'age': 26
    }
}
users
users.items() # .items()
users.keys() # .keys()
for name, info in users.items():
    print(name)
    print(info)
for name, info in users.items():
    print(f"{name}, {info['fullName']} is {info['age']} years old.")

# set 集合 无序，不重复元素序列
colors = {'red', 'green', 'yellow', 'red'}
print(colors)
## 集合的运算
a = set('abcdr')
b = set('aclzm')
print(a - b) 
sorted(a|b) # a+b
print(a&b) # a交b
print(a^b) # 不同时包含于a b
a.add('add') # add 
a
a.update({1,3}) # update
a
a.remove('a') # remove the elements in the set or will generate error
a
a.discard('something not in the set') # even the things you want to delete is not in the set, you can use this function with retrning error
a.clear() # remove
a
aset = {2,3,4,5,6}
bset = {5,6,7,8,9}
aset.intersection(bset)
aset.union(bset)
aset.difference(bset)
bset.difference(aset)