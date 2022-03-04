

# 命名规范
# 类：CamelCase
# object/module: snake_case



# 1.class类 & instance实例: attribute属性 and method方法(可理解为class内的function)
from ossaudiodev import SOUND_MIXER_ALTPCM
from this import d

from sympy import principal_branch


class person:
    # attribute
    name = 'Jacobe'
    age = 39
    # method
    def greet(self): # self
        print(f"Hello, my name is {self.name}, I'm {self.age} years old.")

# create an object 创建具体实例，避免修改原始模板class
# 即使 object.method() 和 class().method() 运行得出同样的结果
p1 = person()
# call the method
p1.greet()
person().greet()

# change attribution
p1.name = "test" # it's the same as `person.name = "test"`
p1.greet()

# delete object
del p1


# 初始化对象 __init__(special method) 是实例创建时最先被调用的函数，每次创建实例都会被调用且它的__init__都会被调用，且第一个参数永远是self
class person:
    def __init__(self):
        self.name = 'Alex'
    def greet(self):
        print(f"Hello, I'm {self.name}")

p2 = person()
p2.greet()

# 在__init__中添加其他参数使初始化更灵活（不固定，在创建实例时可以修改参数）
class person:
    def __init__(self, add_name):
        self.name = add_name
    def greet(self):
        print(f"Hello, I'm {self.name}")

p3 = person("David")
p3.greet()



# 2. inheritance（可修改复制） & polymorphism
class animal():
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"Hello, I'm a {self.name}")

animal_ob = animal("animal")
animal_ob.greet()

class dog(animal):
    def greet(self):
        print(f"Wang... Wang... I'm a {self.name}")

dog_ob = dog("dog")
dog_ob.greet()

class cat(animal):
    def greet(self):
        print("Miao... miao... I am a %s" %self.name)
cat_ob = cat("cat")
cat_ob.greet()

# define function 来调用 method
def hello(animal):
    animal.greet()
hello(animal_ob)
hello(dog_ob)
hello(cat_ob)


# add new attribute and method
class Animal():
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound 
    def greet(self):
        print(f"{self.sound}, I'm a {self.name}")
    def method(self):
        print("This is the new method in class animal")
animal_ob = Animal('cat', 'miao')
animal_ob.greet()
animal_ob.method()
ani_dog_ob = Animal('dog', 'wang... wang')

# 再次示例 define function 来调用class中只想要使用的method，function中的参数要是实例object
def method_animal(Animal):
    Animal.method()
method_animal(animal_ob)
method_animal(ani_dog_ob)


# 3. ? iterators
class Fib():
    def __init__(self):
        self.a = 0
        self.b = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a
    
fib = Fib()

fibRes = []
for i in fib:
    if i > 30:
        break
    fibRes.append(i)
print(fibRes)

# 🚫访问 underscore
class Underscore():
    def __init__(self, name):
        self.__name = name # 限制外界访问name变量
    def method(self):
        print(f"Hello, this is the class which restrict to access the {self.name}")
underscore = Underscore('restrict name')
# underscore.__name 报错
animal_ob.name
animal_ob.sound

# ############################
# ?模块调用 -> go to moduleCall.py

# Python标准库（Python standard library）
from random import randint, choice
randint(1,9)
players = ['alice', 'david','charles', 'michael']
choice(players)

# ##################################
# ? pip install package to use the library online
# e.g. pip3 install pillow
from PIL import Image, ImageFilter

# im = Image.open("/Users/zoeydy/techGit/turingPython/photo..jpg")
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('blur.jpg', 'jpeg')




# exercise
class Car():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def method(self):
        print(f"The info of the car is: \nbrand: {self.brand}, model: {self.model}, year: {self.year}")

car = Car("lanbo", "model", 1990)
car.method()
# import + 修改