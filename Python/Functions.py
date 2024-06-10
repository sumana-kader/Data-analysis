
# def hello():
#     print('welcome to ipcs')
# hello()

# def evenorodd(x):
#     if(x%2==0):
#         print('even')
#     else:
#         print('odd')
# evenorodd(6)
# evenorodd(9)

# def myfunction(x,y=50):
#     print('x:',x)
#     print('y:',y)
# myfunction(y=10,x=2)

# def student(firstname,lastname):
#     print(firstname,lastname)
# student(firstname='hello',lastname='python')
# student(lastname='programme',firstname='python')
# student('good','morning')

# def myfunction(*kids):
#     print('the youngest child is '+  kids[2])
# myfunction('emily','thomas','linus')

# def myfunction(*argv):
#     for x in argv:
#         print(x)
# myfunction('hello','python','programme')

# def myfunction(**student):
#     print('his first name is '+ student['fname'])
#     print('his last name is '+student['lname'])
# myfunction(fname='vignesh',lname='s')

# def myfunction(**kwargs):
#     for key,value in kwargs.items():
#         print('%s=%s'%(key,value))
# myfunction(first='welcome',mid='for',last='course')

# def myfunction(country='Norway'):
#     print('iam from '+country)
# myfunction()
# myfunction('Sweden')
# myfunction('Brazil')

# def myfuntion(xyz):
#     for x in xyz:
#         print(x)
# fruits=['apple','banana','cherry']
# myfuntion(fruits)

# def square_value(num):
#     return num**2
# print(square_value(2))
# print(square_value(-4))

# def myfunction(x):
#     x[0]=30
# lst=[9,11,13,14,15]
# myfunction(lst)
# print(lst)

# def f1():
#     s='i love python'
#     def f2():
#         print(s)
#     f2()
# f1()

# string='hello python'
# print(lambda string:string)

# x='hello python'
# (lambda x:print(x))(x)

# def cube(y):
#     return y*y*y;
# g=lambda x:x*x*x
# print(g(6))
# print(cube(6))

# def power(n):
#     return lambda a:a**n;
# base=power(2)
# print('power is set to 2')
# print(base(6))
# base=power(3)
# print('power is set to 3')
# print(base(5))

# a=[100,2,8,13,15,19,39,70]
# filtered=filter(lambda x:x%2==0,a)
# print(list(filtered))
# maped=map(lambda x:x%2==0,a)
# print(list(maped))

# def myfunction():
#     print(s)
# s='i love python'
# myfunction()

# def myfunction():
#     s='Me too'
#     print(s)
# s='i love python'
# print(s)
# s='hello'
# print(s)
# myfunction()

# a=1
# def f():
#     print('inside f():',a)
# def g():
#     a=2
#     print('inside g():',a)
# def h():
#     global a
#     a=3
#     print('inside h():',a)
# print('global:',a)
# f()
# print('global:',a)
# g()
# print('global:',a)
# h()
# print('global:',a)

# def shout(text):
#     return text.upper()
# print(shout('Hello'))
# yell=shout
# print(yell('hello'))

# def shout(text):
#     return text.upper()
# def whisper(text):
#     return text.lower()
# def greet(func):
#     greeting=func('hello python')
#     print(greeting)
# greet(shout)
# greet(whisper)

# def create_adder(x):
#     def adder(y):
#         return x+y
#     return adder
# add_15=create_adder(15)
# print(add_15(10))

# def calc_factorial(x):
#     if x==1:
#         return 1
#     else:
#         return (x*calc_factorial(x-1))
# num=4
# print('factorial of',num,'is',calc_factorial(num))
# num=3
# print('factorial of',num,'is',calc_factorial(num))


# def add(x,y):
#     return (x+y)
# def subtract(x,y):
#     return (x-y)
# print(add(10,2))
# print(subtract(8,3))

'''
Module
'''

# from math import sqrt,factorial
# print(sqrt(16))
# print(factorial(4))

# import math
# print(dir(math))

