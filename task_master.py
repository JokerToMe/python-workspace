# -*- coding:utf-8 -*-
# s1 = 72
# s2 = 85
# r = (s2 - s1)/s1*100
# print('小明成绩提升的百分点是%.1f%%' %r)

# classmates = ['lucy','Jack','Micheal','Tom']
# classmates.append('lucky')
# classmates.insert(0,'Shine')
# classmates.pop()
# classmates.pop(1)
# classmates[0] = 'Nick'
# print(classmates)

# s = input('birth:')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

# height = 1.75
# weight = 80.5
# bmi = weight/(height*height)
# print('bmi:',bmi)
# if bmi < 18.5:
#     print('过轻')
# elif bmi < 25:
#     print('正常')
# elif bmi < 28:
#     print('过重')
# elif bmi < 32:
#     print('肥胖')
# else :
#     print('严重肥胖')

# names = ['Michael','Lucy','Fancy']
# for name in names:
#     print(name)

# sum = 0
# for i in [1,2,3,4,5,6,7,8,9,10]:
#     sum = sum + i
# print('sum:',sum)

# print(list(range(5)))

# sum = 0
# for x in list(range(101)):
#     sum = sum + x
# print('sum:',sum)

# d = {'Michael':95,'Bob':56,'Tracy':60}
# print('Michael:',d['Michael'])
# print('Toms' in d)
# print(d.get('Toms'))
# print(d.get('Toms',-1))

# d.pop('Michael')
# print(d)

# s = set([1,2,3,4,2,3])
# s.add(5)
# s.add(3)
# s.remove(4)
# print('s:',s)
# t = set([2,5,6])
# print('交集：',s&t)
# print('并集：',s|t)

# a = 'abc'
# b = a.replace('a','A')
# print('a:',a)
# print('b:',b)

# a = ['c','b','a']
# a.sort()
# print(a)

# t = (1,2,3)
# t = (1,2,[1,2])
# d = {'key1':2}
# s = set([1,2,3])
# d[t] = 3
# print('d:',d)
# s.add(t)
# print('s:',s)

# def my_func(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('bad operand type')
#     if x>0:
#         return x
#     else: 
#         return -x

# print(my_func('abs'))

# print(abs('abd'))

# def func():
#     pass

# import math
# def move(x,y,step,angle=0):
#     nx = x + math.cos(angle)*step
#     ny = y + math.sin(angle)*step
#     return nx,ny
# print(move(0,0,2))

# import math
# def quadratic(a,b,c):
#     d = b**2-4*a*c
#     if d >= 0:
#         n = math.sqrt(d)
#         x1 = (-b+n)/(2*a*c)
#         x2 = (-b-n)/(2*a*c)
#         #有两个不相等的实根解
#         if d == 0:
#             print('有两个相等的实根解：')
#         #有两个相等的实根解
#         else:
#             print('有两个不相等的实根解：')   
#         return x1,x2
#     #无实根解
#     else:
#         print('无实根解!')
#         return
# print(quadratic(1,4,1))

# def power(x,n):
#     # s = 1
#     # while n > 0:
#     #     n = n - 1
#     #     s = s * x
#     s = x**n
#     return s
# print('x的n次方等于：',power(3,4))

# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n*n
#     return sum

# numbers = (1,2,3,4)
# print('sum:',calc(*numbers))
# print('可变参数调用的结果：',calc(1,2,3,4,5))

# def person(name,age,**kw):
#     print('name',name,'age',age,'other',kw)

# person('Michael',70)
# person('Michael',70,city='beijing',birthday='1993')

# extra = {'gender':'M','school':'Wuhan University'}
# person('Michael',70,**extra)

# def product(*numbers):
#     pro = 1
#     for n in numbers:
#         pro = pro * n
#     print('乘积为：',pro)

# def sum(a=[]):
#     a.append('end')
#     return a
# print('sum:',sum())    
# print('sum:',sum()) 
# print('sum:',sum()) 

# def fact(n):
#     return fact_iter(n,1)
# def fact_iter(num,product):
#     if num == 1:
#         return product
#     else:
#         return fact_iter(num - 1,num*product)

# print(fact(5))

# L = list(range(100))
# print(L)
# print('取前10个数：',L[:10])
# print('取后10个数：',L[-10:])
# print('取前11到20个数：',L[10:20])
# print(L[:10:2])
# print(L[::5])
# print(L[:])

# print((1,2,3,4,5)[:3])
# print('ABCDEFG'[::2])

# def trim(str):
#     if str =='':
#         print('该字符串为空')
#     elif str[0] == ' ':
#         return trim(str[1:])
#     elif str[-1] == ' ':
#         return trim(str[:-1])
#     else:
#         return str

# str = input('请输入：')
# print('结果为'+trim(str))

# from collections import Iterable
# print(isinstance('abc', Iterable))
# print(isinstance([],Iterable))
# print(isinstance(123,Iterable))

# for i,value in enumerate(['A','B','C']):
#     print(i,value)

# for x,y,z in [(1,2,3),(3,4,6),(5,6,7)]:
#     print(x,y,z)

# def findMinAndMax(L):
#     min = L[0]
#     max = L[0]  
#     for value in L:
#         if value < min:
#             min = value
#         if value > max:
#             max = value
#     return (min,max)

# print(findMinAndMax([1,2,3,4,5]))

# print([x*x for x in range(1,11) if x%2 == 0])
# print([x**3 for x in range(1,11)])
# print([m+n for m in ['A','B','C'] for n in ['a','b','c']])

# import os
# print([d for d in os.listdir('..')])
# d = {'x':1,'y':2,'z':3}
# for k,v in d.items():
#     print(k,'=',v)
# print([k+'='+str(v) for k,v in d.items()])

# L = ['Hello','World',18]
# print([s.lower() for s in L if isinstance(s,str)])

# g = (x*x for x in range(1,11))
# for n in g:
#     print(n)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# def fib(max):
#     n,a,b = 0,0,1
#     while n < max:
#         yield a+b
#         a,b = b,a+b
#         n = n+1
#     return 'done'

# g = fib(8)
# while True:
#     try:
#         print(next(g))
#     except StopIteration as e:
#         print(e.value)
#         break
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# for n in fib(8):
#     print(n)

# def odd():
#     print('step1')
#     yield 1
#     print('step2')
#     yield 2
#     print('step3')
#     yield 3
# o = odd()
# next(o)
# next(o)
# next(o)

# from collections import Iterator
# print(isinstance(iter([x for x in range(10)]),Iterator))
# print(isinstance((x for x in range(10)),Iterator))

# def add(x,y,f):
#     return f(x)+f(y)

# print(add(5,-10,abs))

# print(list(map(str,[1,2,3,4])))
# def f(x):
#     return x**2
# print(list(map(f,[1,2,3,4])))

#将数字字符串转化为int类型
# from functools import reduce
# def f1(x,y):
#     return x*10+y
# def f2(s):
#     digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
#     return digits[s]

# print(isinstance(reduce(f1,map(f2,'56923')),int))

# def normalize(s):
#     return s.capitalize()

# print(list(map(lambda s:s.capitalize(),['adam', 'LISA', 'barT'])))

# from functools import reduce
# print(reduce(lambda x,y: x*y,[1,2,3,4]))

# s = '123.456'
# digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':None}
# def f1(s):
#     return digits[s]
# def f2(x,y):
#     return x*10+y
# L = list(map(f1,s))
# index = L.index(None)
# L1 = L[:index]
# L2 = L[index+1:]
# print(reduce(f2,L1)+reduce(f2,L2)*0.1**len(L2))

# def is_odd(n):
#     return n%2 == 1
# print(list(filter(is_odd,[1,2,3,4,5])))

# #生成一个从3开始的奇数数列
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n

# #筛选不能不能被n整除的数
# def _not_disivible(n):
#     return lambda x: x%n > 1

# #创建一个生成素数的生成器
# def primes():
#     #第一个数为2，直接输出
#     yield 2
#     #获取原始的奇数数列
#     t = _odd_iter()
#     #通过循环不断输出
#     while True:
#         n = next(t)
#         yield n
#         #用取出的素质作为筛选条件再次筛选
#         t = filter(_not_disivible(n),t)
# n = 0
# p = primes()
# while n < 10:
#     print('第'+str(n+1)+'个素数为：',next(p))
#     n = n + 1

#创建一个1到n的自然数序列
# def natural(x):
#     n = 1
#     while n <= x:
#         yield n
#         n = n + 1
# def _is_reverse(x):
#     return x == int(str(x)[::-1])

# print(list(filter(_is_reverse,natural(1000))))

# print(sorted([36, 5, -12, 9, -21],key = abs))
# print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower))
# print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True))

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]  
# print(sorted(L,key=lambda s:s[0]))
# print(sorted(L,key=lambda s:s[1],reverse=True))
    
# def count():
#     fs = []
#     for i in range(1,4):
#         def f():
#             return i*i
#         fs.append(f)
#     return fs

# t = count()
# print(t[0](),t[1](),t[2]())

# def count():
#     def g(i):
#         return lambda:i*i
#     fs = []
#     for i in range(1,4):
#         fs.append(g(i))
#     return fs

# f1,f2,f3 = count()
# print(f1(),f2(),f3())

# print([x**2 for x in range(1,4)])

# from functools import reduce
# def is_odd(n):
#     return n % 2 == 1

# L1 = list(filter(is_odd, range(1, 20)))
# print('L1',L1)
# L2 = list(filter(lambda n:n%2==1,range(1,20)))
# print('L2',L2)
# L3 = list(map(lambda n:n**2,range(1,20)))
# print('L3',L3)
# L4 = reduce(lambda x,y:x+y,range(1,4))
# print('L4',L4)


# class Dog(Animal):
#     def run(self):
#         print('Dog is running')

# class Cat(Animal):
#     def run(self):
#         print('Cat is running')

# def run_twice(animal):
#     animal.run()
#     animal.run()
# #file-like object 动态语言的鸭子类型
# class Tree(object):
#     def run(self):
#         print('Tree can\'t run')

# dog = Dog()
# cat = Cat()
# tree = Tree()
# run_twice(animal)
# run_twice(dog)
# run_twice(cat)
# run_twice(tree)

# print(isinstance(animal,Animal))
# print(isinstance(dog,Animal))

# print(type(123))
# print(type('123'))
# print(type(None))

# import types
# def fn():
#     pass
# print('fn',type(fn)==types.FunctionType)
# print('abs',type(abs)==types.BuiltinFunctionType)
# print('lambda x:x',type(lambda x:x)==types.LambdaType)
# print('for',type((x for x in range(10)))==types.GeneratorType)

# print(dir('ABC'))
# print(len('ABC'))
# print('ABC'.__len__())

# class Dog(object):
#     def __len__(self):
#         return 100
# d = Dog()
# print(len(d))
# print(d.__len__())

# class MyObject(object):

#     def __init__(self):
#         self.x = 9

#     def power(self):
#         return self.x**2

# my_object = MyObject()
# print(hasattr(my_object,'x'))
# print(my_object.x)
# setattr(my_object,'x',19)

# print(hasattr(my_object,'power'))
# print(getattr(my_object,'power'))
# print(my_object.power())
# power = getattr(my_object,'power')
# print(power())
# print(hasattr(my_object,'__init__'))
# __init__ = getattr(my_object,'__init__')
# print(__init__)

# class Student(object):
#     name = 'Student'

# s = Student()
# print(s.name)
# print(Student.name)
# s.name = 'Michael'
# print(s.name)
# print(Student.name)
# del s.name
# print(s.name)
# print(Student.name)

# class Student(object):
#     count = 0

#     def __init__(self,name):
#         self.name = name

# s1 = Student('Michael')
# Student.count = Student.count+1
# s2 = Student('Michael')
# Student.count = Student.count+1
# print(Student.count)

# from types import MethodType

# class Student(object):
#     pass

# s = Student()
# s.name = 'Michael'
# print(s.name)

# def set_age(self,age):
#     self.age = age

# s.set_age = MethodType(set_age,s)
# s.set_age(26)
# print(s.age)

# s2 = Student()
# s2.set_age(25)
# Student.set_age = set_age
# s.set_age(20)
# s2.set_age(25)
# print(s.age)
# print(s2.age)

# class Student(object):
#     __slots__ = ('name','age')

# s = Student()
# s.name = 'Michael'
# s.age = 20
# print('name',s.name)
# print('age',s.age)
# # s.score = 90
# # print('score',s.score)

# class GraduateStudent(Student):
#     pass

# gs = GraduateStudent()
# gs.score = 90
# print(gs.score)

# class Student(object):

#     @property
#     def score(self):
#         return self._score

#     @score.setter
#     def score(self,score):
#         if not isinstance(score,int):
#             raise ValueError('score must be integer')
#         if score <0 or score>100:
#             raise ValueError('score must be between 0~100')
#         self._score = score

# s = Student()
# s.score = 20
# print(s.score)

# class Student(object):

#     @property
#     def birth(self):
#         return self._birth
    
#     @birth.setter
#     def birth(self,birth):
#         self._birth = birth

#     @property
#     def age(self):
#         return 2019-self._birth

# class Screen(object):

#     @property
#     def width(self):
#         return self._width

#     @width.setter
#     def width(self,width):
#         if not isinstance(width,int):
#             raise ValueError('width must be integer')
#         if width < 0:
#             raise ValueError('width must be greater than zero')
#         self._width = width

#     @property
#     def height(self):
#         return self._height

#     @height.setter
#     def height(self,height):
#         if not isinstance(height,int):
#             raise ValueError('height must be integer')
#         if height < 0:
#             raise ValueError('height must be greater than zero')
#         self._height = height

#     @property
#     def resolution(self):
#         return self._width*self._height

# s = Screen()
# s.width = 1024
# s.height = 768
# print(s.resolution)

# class Student(object):

#     def __init__(self,name):
#         self.name = name

#     def __str__(self):
#         return 'Student Object (name:%s)' % self.name

#     __repr__ = __str__

# s = Student('Michael')
# print(s)

# class Fib(object):

#     def __init__(self):
#         self.a,self.b = 0,1

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.a,self.b = self.b,self.a+self.b
#         if self.a > 10000:
#             raise StopIteration
#         return self.a
    
#     def __getitem__(self,n):
#         a,b = 1,1
#         for x in range(n):
#             a,b = b,a+b
#         return a

# for x in Fib():
#     print(x)

# f = Fib()
# print(f[3])

# class Student(object):

#     def __init__(self):
#         self.name = 'Michael'

#     def __getattr__(self,attr):
#         if attr == 'score':
#             return 90
#         elif attr == 'age':
#             return lambda:25
#         else:
#             raise AttributeError('\'Student\' object has no attribute %s' % attr)

# s = Student()
# print(s.score)  
# a = s.age
# print(a()) 
# print(s.gender)        

# class Chain(object):

#     def __init__(self,path=''):
#         self._path = path

#     def __getattr__(self,path):
#         # if path == 'user':
#         #     return lambda x: Chain('%s/%s' %(self._path,x))
#         return Chain('%s/%s' % (self._path,path))
    
#     def __str__(self):
#         return self._path

#     def user(self,path):
#         return Chain('%s/%s' % (self._path,path))

#     __repr__ = __str__

# print(Chain().status.user('hello').timeline.list)

# class Student(object):
#     def __init__(self,name):
#         self.name = name

#     def __call__(self):
#         print('My name is %s' % self.name)

# s = Student('Michael')
# s()

# from enum import Enum
# # Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# Month = Enum('Month', ('11', '22', '33', '44', '55'))

# for name,member in Month.__members__.items():
#     print(name,'=>',member,',',member.value)

# from enum import Enum,unique

# @unique
# class Week(Enum):
#     s = 1
#     m = 2
#     n = 3

# print(Week.s)
# print(Week['s'])
# print(Week.m.value)
# print(Week(3))

# def fn(self,name='world'):#定义函数
#     print('Hello %s' % name)

# Hello = type('Hello',(object,),dict(hello=fn))#创建Hello Class
# h = Hello()
# h.hello()

# class FlyAnimal(object):
    
#     def fly(self,name):
#         print('%s is flying' % name)

# class RunAnimal(object):

#     def run(self,name):
#         print('%s is running' % name)

# def eat(self):
#     print('chicken is eating food')

# Chicken = type('Chicken',(FlyAnimal,RunAnimal),dict(eat=eat))
# c = Chicken()
# c.fly('chicken')
# c.run('chicken')
# c.eat()

# try:
#     print('try...')
#     r = 10/0
#     print('result',r)
# except ZeroDivisionError as e:
#     print('exception',e)
# finally:
#     print('finally...')
# print('end...')

# from functools import reduce

# def str2num(s):
#     return float(s)

# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)

# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 7.6')
#     print('99 + 88 + 7.6 =', r)

# try:
#     main()
# except ValueError as e:
#     print(e)

# import pdb

# s = '0'
# n = int(s)
# pdb.set_trace()
# print(10/n)

# class Dict(dict):

#     def __init__(self,**kw):
#         super.__init__(self,**kw)

#     def __getattr__(self,key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError('Dict object has no attribute %s' % key)

#     def __setattr__(self,key,value):
#         self[key] = value

# import re
# m = re.search('(?<abc)def','abcdef')
# print(m.group(0))

# f = open('./text.txt','r')
# print(f.read())
# f.close()

# with open('./text.txt','r') as f:
#     # for line in f.readlines():
#     #     print(line.strip())
#     print(f.read())

# with open('./icon.jpg','rb') as f:
#     print(f.read())

# with open('C:\\Windows\\system.ini','r') as f:
#     print(f.read())

# from io import StringIO

# # f = StringIO()
# # print(f.write('Hello'))
# # print(f.write(' '))
# # print(f.write('World'))
# # print(f.getvalue())

# f = StringIO('Hello\nHi\nWorld')
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())

# from io import BytesIO

# f = BytesIO()
# print(f.write('中文'.encode('utf-8')))
# print(f.getvalue())

# f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# print(f.getvalue())

#环境变量
# import os
# print(os.environ.get('x','default'))
# print(os.path.abspath('.'))
# #创建一个完整路径
# new_path = os.path.join('C:\\Users\\Administrator\\Desktop','testdir')
# print(new_path)
# #创建目录
# os.mkdir(new_path)
# #删除这个目录
# os.rmdir(new_path)

# print(os.path.split('C:\\Users\\Administrator\\Desktop\\icon.jpg'))
# print(os.path.splitext('C:\\Users\\Administrator\\Desktop\\icon.jpg'))
# os.rename('C:\\Users\\Administrator\\Desktop\\test.txt','C:\\Users\\Administrator\\Desktop\\test.py')
# os.remove('C:\\Users\\Administrator\\Desktop\\test.py')

# print([x for x in os.listdir('.') if os.path.isfile(x)])
# fl = [x for x in os.listdir('..')]
# print(fl)
# print([x for x in fl if os.path.isdir(x)])
# print([x for x in fl if os.path.isfile(x)])

# import pickle
# d = dict(name='Bob',age=20,score=88)
# #序列化为二进制字节码
# b = pickle.dumps(d)
# print(b)
# print(pickle.loads(b))
# #序列化为二进制字节码并存入文件pickling
# with open('dump.txt','wb') as f:
#     pickle.dump(d,f)
# #读取文件内容并反序列化unpickling
# with open('dump.txt','rb') as f:
#     print(pickle.load(f))

# import json
# # d = dict(name='Bob',age=20,score=88)
# # print(json.dumps(d))
# # json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# # print(json.loads(json_str))

# class Student(object):

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# s = Student('Bob',20)  

# def student2dict(stu):
#     return {
#         'name': stu.name,
#         'age': stu.age
#     }
# class Teacher(object):
    
#     def __init__(self,gender,city):
#         self.gender = gender
#         self.city = city

# t = Teacher('woman','shanghai')
# #将类实例序列化为json对象时，首先将实例转化为dict，再将dict转化为json
# print(json.dumps(s,default=student2dict))
# print(json.dumps(s,default=lambda obj:obj.__dict__))
# print(json.dumps(t,default=lambda x: x.__dict__))

# def dict2student(str):
#     return Student(str['name'],str['age'])

# json_str = '{"name":"Bob","age":20}'
# print(json.loads(json_str,object_hook=dict2student))

# from multiprocessing import Process
# import os

# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')

# from multiprocessing import Pool
# import os,time,random

# def long_time_task(name):
#     print('Runt task %s (%s)...' % (name,os.getpid()))
#     start = time.time()
#     time.sleep(random.random()*3)
#     end = time.time()
#     print('Task %s run %0.2f seconds' % (name,end-start))

# if __name__ == '__main__':
#     print('Parent process %s' % os.getpid)
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task,args=(i,))
#     print('Waitting for all subprocesses done')
#     p.close()
#     p.join()
#     print('All subprocesses done')

# import subprocess
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup','www.python.org'])
# print('Exit code',r)

# from multiprocessing import Process,Queue
# import os,time,random

# #写数据进程执行的代码
# def write(q):
#     print('Process to write: %s' % os.getpid)
#     for value in ['A','B','C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())

# #读数据进程执行的代码
# def read(q):
#     print('Process to read: %s' % os.getpid)
#     while True:
#         value = q.get(True)
#         print('Get %s from queue' % value)

# if __name__ == '__main__':
#     #父进程创建Queue并传给子进程
#     q = Queue()
#     pw = Process(target=write,args=(q,))
#     pr = Process(target=read,args=(q,))
#     #启动子进程pw写入
#     pw.start()
#     #启动子进程pr读取
#     pr.start()
#     #等待进程结束
#     pw.join()
#     #pr进程是死循环，无法结束，强行终止
#     pr.terminate()

# from multiprocessing import Process,Queue
# import os,time,random

# #写进程
# def write(q):
#     print('Process to write: %s' % os.getpid)
#     for value in ['a','b','c']:
#         print('Put %s to queue' % value)
#         q.put(value)
#         time.sleep(random.random())

# #读进程
# def read(q):
#     print('Process to read: %s' % os.getpid)
#     while True:
#         value = q.get(True)
#         print('Get %s from queue' % value)

# if __name__ == '__main__':
#     #创建Queue传入子进程
#     q = Queue()
#     #写
#     pw = Process(target=write,args=(q,))
#     #读
#     pr = Process(target=read,args=(q,))
#     #开始写
#     pw.start()
#     #开始读
#     pr.start()
#     #等待写结束
#     pw.join()
#     #死循环，强制终止
#     pr.terminate()

# import threading,time

# def loop():
#     print('Thread %s is running' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('Thread %s >>> %s' % (threading.current_thread().name,n))
#         time.sleep(1)
#     print('Thread %s ended' % threading.current_thread().name)

# print('Thread %s is running' % threading.current_thread().name)
# t = threading.Thread(target=loop,name='LoopThread')
# t.start()
# t.join()
# print('Thread %s ended' % threading.current_thread().name)

# import threading,time
# #银行存款
# balance = 0
# lock = threading.Lock()
# def change_it(n):
#     #先存后取，结果应该为0
#     global balance
#     balance = balance + n
#     balance = balance - n
# def run_thread(n):
#     for i in range(10000000):
#         lock.acquire()
#         try:
#             change_it(n)
#         finally:
#             lock.release()
        

# t1 = threading.Thread(target=run_thread,args=(5,))
# t2 = threading.Thread(target=run_thread,args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

# import threading

# school_local = threading.local()

# def process_student():
#     stu = school_local.student
#     print('Hello! %s (in %s)' % (stu,threading.current_thread().name))

# def process_thread(name):
#     school_local.student = name
#     process_student()

# t1 = threading.Thread(target=process_thread,args=('Shine',))
# t2 = threading.Thread(target=process_thread,args=('Nick',))
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# import random,time,queue
# from multiprocessing.managers import BaseManager

# #发送任务的队列
# task_queue = queue.Queue()
# #接收结果的队列
# result_queue = queue.Queue()

# #从BaseManager继承的QueueManager
# class QueueManager(BaseManager):
#     pass

# #把两个Queue都注册在网络上，callable对象关联了Queue对象
# QueueManager.register('get_task_queue',callable=lambda: task_queue)
# QueueManager.register('get_result_queue',callable=lambda: result_queue)
# #绑定端口5000，设置验证码abc
# manager = QueueManager(address=('',5000),authkey=b'abc')
# #启动queue
# manager.start()
# #活的通过网络访问的queue对象
# task = manager.get_task_queue()
# result = manager.get_result_queue()
# #放几个任务
# for i in range(10):
#     n = random.randint(0,10000)
#     print('Put task %d...' % n)
#     task.put(n)
# #从result队列读取结果
# print('Try get results...')
# for i in range(10):
#     r = result.get(timeout=10)
#     print('Result %d...' % r)
# #关闭
# manager.shutdown()
# print('Master exit...')

# task_master.py

# import random, time, queue
# from multiprocessing.managers import BaseManager

# # 发送任务的队列:
# task_queue = queue.Queue()
# # 接收结果的队列:
# result_queue = queue.Queue()

# # 从BaseManager继承的QueueManager:
# class QueueManager(BaseManager):
#     pass

# # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
# QueueManager.register('get_task_queue', callable=lambda: task_queue)
# QueueManager.register('get_result_queue', callable=lambda: result_queue)
# # 绑定端口5000, 设置验证码'abc':
# manager = QueueManager(address=('', 5000), authkey=b'abc')
# # 启动Queue:
# manager.start()
# # 获得通过网络访问的Queue对象:
# task = manager.get_task_queue()
# result = manager.get_result_queue()
# # 放几个任务进去:
# for i in range(10):
#     n = random.randint(0, 10000)
#     print('Put task %d...' % n)
#     task.put(n)
# # 从result队列读取结果:
# print('Try get results...')
# for i in range(10):
#     r = result.get(timeout=10)
#     print('Result: %s' % r)
# # 关闭:
# manager.shutdown()
# print('master exit.')

# import re
# if re.match(r'^\d{3}\-\d{3,8}$','010-12345'):
#     print('success')
# else:
#     print('failure')

# str = 'a,b    c'
# print(re.split(r'[\s\,]+',str))
# m = re.match(r'^(\d{3})-(\d{3,8})$','010-123456')
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))
# m = re.match(r'^(\d+?)(0*)$','123000')
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))

# re_telephoto = re.compile(r'^(\d{3})\-(\d{3,8})$')
# print(re_telephoto.match('101-12356').groups())

# from datetime import datetime
# # print(datetime.now())
# print(datetime.fromtimestamp(1429417200.0))
# print(datetime.strptime('2015-6-1 18:19:59','%Y-%m-%d %H:%M:%S'))
# now = datetime.now()
# print(now.strftime('%a, %b %d %H:%M'))

# from collections import namedtuple
# Point = namedtuple('Point',['X','Y'])
# p = Point(2,3)
# print(p.X)
# print(p.Y)

# print(isinstance(p,Point))
# print(isinstance(p,tuple))
# Circle = namedtuple('Circle',['x','y','r'])

# from collections import deque
# q = deque([0,1,2])
# q.append(3)
# q.appendleft(-1)
# print(q)

# from collections import defaultdict
# d = defaultdict(lambda: 'N/A')
# d['key1'] = 'abc'
# print(d['key1'])
# print(d['key2'])

# from collections import OrderedDict
# od = OrderedDict({'1':1,'2':2})
# od['0'] = 0
# od['3'] = 3
# print(od)


# from collections import OrderedDict

# class LastUpdateOrderedDict(OrderedDict):

#     def __init__(self, capacity):
#         super(LastUpdateOrderedDict,self).__init__()
#         self._capacity = capacity

#     def __setitem__(self,key,value):
#         containsKey = 1 if key in self else 0
#         if len(self) - containsKey >= self._capacity:
#             last = self.popitem(last=False)
#             print('remove',last)
#         if containsKey:
#             del self[key]
#             print('set',(key,value))
#         else:
#             print('add',(key,value))
#         OrderedDict.__setitem__(self,key,value)

# luod = LastUpdateOrderedDict(3)
# luod.__setitem__('0',0)
# luod.__setitem__('1',1)
# luod.__setitem__('2',2)
# luod.__setitem__('1',3)
# print(luod)

# from collections import ChainMap
# import os,argparse

# #构造缺省参数
# defaults = {
#     'color': 'red',
#     'user': 'guest'
# }

# #构造命令行参数
# parser = argparse.ArgumentParser()
# parser.add_argument('-u','--user')
# parser.add_argument('-c','--color')
# nameSpace = parser.parse_args()
# command_line_args = {k:v for k,v in vars(nameSpace).items() if v}
# #组合成ChainMap
# combined = ChainMap(command_line_args,os.environ,defaults)
# print('color=%s' %combined['color'])
# print('user=%s' % combined['user'])

# from collections import Counter

# c = Counter()
# for ch in 'programming':
#     c[ch] = c[ch] + 1
# print(c)

# import hashlib

# def calc_md5(password):
#     md5 = hashlib.md5()
#     md5.update(password.encode('utf-8'))
#     print(md5.hexdigest())

# calc_md5('123456')

# db = {
#     'michael': 'e10adc3949ba59abbe56e057f20f883e',
#     'bob': '878ef96e86145580c38c87f0410ad153',
#     'alice': '99b1c2188db85afee403b1536010c2c9'
# }

# def login(user, password):
#     md5 = hashlib.md5()
#     for k,v in db.items():
#         if k == user:
#             md5.update(password.encode('utf-8'))
#             if v == md5.hexdigest():
#                 print('login success')
#                 return True
#             else:
#                 print('password error')
#                 return False

# login('michael','1234567')

# import itertools
# ns = itertools.repeat('a',4)
# for v in ns:
#     print(v)

# natuals = itertools.count(1)
# ns = itertools.takewhile(lambda x: x<=10,natuals)
# for v in ns:
#     print(v)
# ns = itertools.chain('abc','xyz')
# for v in ns:
#     print(v)
# ns = itertools.groupby('aaacccbbddddAA',lambda c: c.upper())
# for k,group in ns:
#     print(k,list(group))

# t = itertools.count(1,2)

# def pi(n):
#     pi = 0
#     for i in range(n):
#         pi = pi + (-1)**i * 4/next(t)
#     print(pi)

# pi(10000)

# from contextlib import contextmanager

# class Query(object):

#     def __init__(self,name):
#         self.name = name

#     def query(self):
#         print('Query info about %s...' % self.name)

# @contextmanager
# def create_query(name):
#     print('Begin...')
#     q = Query(name)
#     yield q
#     print('End...')

# with Query('Bob') as q:
#     q.query()

# with create_query('Bob') as q:
#     q.query()

# @contextmanager
# def tag(name):
#     print('<%s>' % name)
#     yield
#     print('</%s>' % name)

# with tag('h1'):
#     print('hello world')

# from urllib import request,parse

# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status:',f.status,f.reason)
#     for k,v in f.getheaders():
#         print('%s: %s' % (k,v))
#     print('Data:',data.decode('utf-8'))

#模拟iPhone6去请求豆瓣首页
# req = request.Request('https://api.douban.com/v2/book/2129650')
# req.add_header('User-Agent','Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     print('Status:',f.status,f.reason)
#     for k,v in f.getheaders():
#         print('%s: %s' % (k,v))
#     print('Data:',f.read().decode('utf-8'))

#post请求，模拟微博登录
# print('Login to weibo.cn...')
# email = '240272750@qq.com'
# password = 'Lxy13437141368'
# login_data = parse.urlencode([
#     ('username', email),
#     ('password', password),
#     ('entry', 'mweibo'),
#     ('client_id', ''),
#     ('savestate', '1'),
#     ('ec', ''),
#     ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# ])

# req = request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin', 'https://passport.weibo.cn')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

# with request.urlopen(req) as f:
#     print('Status:',f.status,f.reason)
#     for k,v in f.getheaders():
#         print('%s: %s' % (k,v))
#     print('Data:',f.read().decode('utf-8'))

# from html.parser import HTMLParser
# from html.entities import name2codepoint

# class Myhtmlparser(HTMLParser):

#     def handle_starttag(self,tag,attrs):
#         print('<%s>' % tag)

#     def handle_endtag(self,tag):
#         print('</%s>' % tag)

#     def handle_startendtag(self,tag,attrs):
#         print('<%s/>' % tag)

#     def handle_data(self,data):
#         print(data)

#     def handle_comment(self, data):
#         print('<!--',data,'-->')

#     def handle_entityref(self,name):
#         print('&%s' % name)

#     def handle_charref(self, name):
#         print('&#%s' % name)

# parser = Myhtmlparser()
# parser.feed('''<html>
# <head></head>
# <body>
# <!-- test html parser -->
#     <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
# </body></html>''')

# from PIL import Image
# #打开一个.jpg头像文件
# im = Image.open('icon.jpg')
# print(im.size)
# #获得头像尺寸
# w,h = im.size
# print('Orginal image size: %sx%s' % (w,h))
# #缩放到50%
# im.thumbnail((w//2,h//2))
# print('Resize image to: %sx%s' % (w//2,h/2))
# #把缩放后的头像用jpeg保存
# im.save('thumbneil.jpg','jpeg')

# #设置图片模糊效果
# from PIL import Image,ImageFilter

# #打开jpg文件 
# im = Image.open('icon.jpg')
# #应用模糊滤镜
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('blur.jpg','jpeg')

# #生成字母验证码图片
# from PIL import Image,ImageDraw,ImageFont,ImageFilter

# import random

# #随机字母
# def rnd_char():
#     return chr(random.randint(65,90))

# #随机颜色1
# def rnd_color():
#     return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

# #随机颜色2
# def rnd_color2():
#     return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

# #240x60
# width = 60*4
# height = 60
# image = Image.new('RGB',(width,height),(255,255,255))
# #创建font对象
# font = ImageFont.truetype('Arial.ttf', 36)
# #创建Draw对象
# draw = ImageDraw.Draw(image)
# #填充每个像素
# for x in range(width):
#     for y in range(height):
#         draw.point((x,y),fill=rnd_color())
# #输出文字
# for t in range(4):
#     draw.text((60 * t + 10, 10), rnd_char(), font=font, fill=rnd_color2())
# #模糊
# image = image.filter(ImageFilter.BLUR)
# image.save('code.jpg','j

# import requests
# r = requests.get('https://wwww.douban.com')
# print(r.status_code)

# from tkinter import *
# import tkinter.messagebox as messagebox

# class Application(Frame):

#     def __init__(self, master=None):
#         Frame.__init__(self,master)
#         self.pack()
#         self.createWidgets()

#     def createWidgets(self):
#         self.nameInput = Entry(self)
#         self.nameInput.pack()
#         self.alertButton = Button(self,text='Hello',command=self.hello)
#         self.alertButton.pack()

#     def hello(self):
#         name = self.nameInput.get() or 'world'
#         messagebox.showinfo('Message','Hello %s' % name)

# app = Application()
# app.master.title('Hello,world')
# app.mainloop()

# from turtle import *

# #设置笔刷宽度
# width(4)
# #前进
# forward(200)
# #右转90度
# right(90)
# #笔刷颜色 
# pencolor('red')
# forward(100)
# right(90)
# pencolor('green')
# forward(200)
# right(90)
# pencolor('blue')
# forward(100)
# right(90)

# def draw_star(x,y):
#     pu()
#     goto(x,y)
#     pd()
#     seth(0)
#     for i in range(5):
#         fd(40)
#         rt(144)

# for x in range(0,250,50):
#     draw_star(x,0)

# #设置色彩模式是rgb
# colormode(255)

# lv = 14
# l = 120
# s = 45

# width(lv)
# #初始化rgb颜色
# r = 0
# g = 0
# b = 0
# pencolor(r,g,b)

# penup()
# bk(l)
# pendown()
# fd(l)

# def draw_tree(l,level):
#     global r,g,b
#     #save the current pen width
#     w = width()
#     #narrow the pen width
#     width(w*3.0/4.0)
#     #set color
#     r = r + 1
#     g = g + 1
#     b = b + 1
#     pencolor(r%200,g%200,b%200)
#     l = l*3.0/4.0

#     lt(s)
#     fd(l)

#     if level < lv:
#         draw_tree(l,level+1)
#     bk(l)
#     rt(2*s)
#     fd(l)

#     if level < lv:
#         draw_tree(l,level+1)
#     bk(l)
#     lt(s)

#     #restore the previous pen width
#     width(w)

# speed('fastest')
# draw_tree(l,4)

# #关闭窗口
# done()

import socket

#创建一个socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
s.connect(('www.sina.com.cn',80))
#发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#接收数据
buffer = []
while True:
    #每次最多接收1kb
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
#关闭连接
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
#把接收的数据写入文件
with open('sina.html','wb') as f:
    f.write(html)