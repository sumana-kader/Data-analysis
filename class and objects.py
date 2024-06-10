# class cars:
#     attr1='BMW'
#     attr2='series 1'
#     def fun(self):
#         print('iam from',self.attr1)
#         print('my model is ',self.attr2)
# john=cars()
# print(john.attr1)
# print(john.attr2)
# john.fun()

# class person:
#     def __init__(self,name):
#         self.name=name
#     def say_hi(self):
#         print('hello my name is',self.name)
# p=person('vignesh')
# p.say_hi()

# class Cars:
#     fourwheeler='Cars'
#     def __init__(self,brand,colour):
#         self.brand=brand
#         self.colour=colour
#     def fun(self):
#         print('Hello ',self.brand )
#         print('and my colour is ', self.colour)
# TATA=Cars('Nexon','brown')
# mustang=Cars('ford','orange')
# TATA.fun()
# mustang.fun()
# TATA.colour='red'
# TATA.fun()
# del TATA.colour
# TATA.fun()
# del TATA
# TATA.fun()

# class myclass:
#     def __init__(self):
#         self.hello='hello'
#     def print_hello(self):
#         print(self.hello)
# obj=myclass()
# obj.print_hello()

# class Myclass:
#     first=0
#     second=0
#     answer=0
#     def __init__(self,f,s):
#         self.first=f
#         self.second=s
#     def display(self):
#         print('First number= '+str(self.first))
#         print('Second number= '+ str(self.second))
#         print('Addition of 2 number ='+ str(self.answer))
#     def calculate(self):
#         self.answer=self.first+self.second
# obj=Myclass(200,200)
# obj.calculate()
# obj.display()

# class Employee:
#     def __init__(self):
#         print('employee created')
#     def __del__(self):
#         print('destructor called,employee deleted')
# obj=Employee()
# del obj

# class Employee:
#     def __init__(self):
#      print('employee created')
#     def __del__(self):
#      print('destructor called')
# def create_obj() -> object:
#     print('making object...')
#     obj=Employee()
#     print('function end...')
#     return obj
# print('calling create_obj()function...')
# obj= create_obj()
# print('programme end')

# class employee:
#     def __init__(self):
#         print('employee created')
#     def __del__(self):
#         print('destructor called')
# def create_obj():
#     print('making object')
#     obj=employee()
#     print('function end')
#     return obj
# print('calling create_obj()function')
# obj=create_obj()
# print('programme end')