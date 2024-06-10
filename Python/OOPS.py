
# from prime import primeornot
# from prime import evenorodd
# from prime import  *
# import prime
# # num = int(input('Enter a Number : '))
# # # prime.primeornot()
# # prime.primeornot(num)
# #
# # check = int(input("Enter a number : "))
# # prime.evenorodd(check)

# class myclass:
#     __hiddenvariable=0
#     def add(self, increment):
#         self.__hiddenvariable+=increment
#         print(self.__hiddenvariable)
# myobject=myclass()
# myobject.add(2)
# myobject.add(5)
# print(myobject.__hiddenvariable)

# class myclass:
#     __hiddenvariable=10
# myobject=myclass()
# print(myobject._myclass__hiddenvariable)

# class counter:
#     def __init__(self):
#         self.current=0
#     def increment(self):
#         self.current+=1
#     def value(self):
#         return self.current
#     def reset(self):
#         self.current=0
# counter=counter()
# counter.increment()
# counter.increment()
# counter.increment()
# print(counter.value())
# # print(counter.__current)
# from prime import primeornot
# num=int(input('enter:'))
# primeornot(num)

# class person(object):
#     def __init__(self,name):
#         self.name=name
#     def getname(self):
#         return self.name
#     def isemployee(self):
#         return False
# class employee(person):
#     def isemployee(self):
#         return True
# emp=person('sathya')
# print(emp.getname(),emp.isemployee())
# emp=employee('vignesh')
# print(emp.getname(),emp.isemployee())

# class person(object):
#     def __init__(self,name,idnumber):
#         self.name= name
#         self.idnumber= idnumber
#     def display(self):
#         print(self.name)
#         print(self.idnumber)
# class employee(person):
#     def __init__(self,name,idnumber,salary,post):
#         self.salary=salary
#         self.post=post
#         person.__init__(self,name,idnumber)
# a=employee('vignesh',9768237,2000,'intern')
# a.display()


# class base(object):
#     def __init__(self,name):
#         self.name=name
#     def getname(self):
#         return self.name
# class child(base):
#     def __init__(self,name,age):
#         base.__init__(self,name)
#         self.age=age
#     def getage(self):
#         return self.age
# class grandchild(child):
#     def __init__(self,name,age,adress):
#         child.__init__(self,name,age)
#         self.adress=adress
#     def getadress(self):
#         return self.adress
# # g=grandchild('vignesh',23,'tvpm')
# print(g.getname(),g.getage(),g.getadress())

# obj1 = base('vignesh')
# obj1.getname()








# class Base1(object):
#     def __init__(self):
#         self.str1='hello'
#         print('Base1')
# class Base3(object):
#     def __init__(self):
#         self.str3='hy'
#         print('Base2')
# class derived(Base3,Base1):
#     def __init__(self):
#         Base3.__init__(self)
#         Base1.__init__(self)
#         print('derived')
#     def printStrs(self):
#         print(self.str3,self.str1)
# ob=derived()
# ob.printStrs()


# class father():
#     def __init__(self,father_name):
#         self.father_name=father_name
#         print('father class' )
# class mother():
#     def __init__(self,mother_name):
#         self.mother_name=mother_name
#         print('mother class')
# class daughter(father,mother):
#     def __init__(self,father_name,mother_name,daughter_name):
#         father.__init__(self,father_name)
#         mother.__init__(self,mother_name)
#         self.daughter_name=daughter_name
#         print('daughter')
#     def print_parent_name(self):
#         print(self.father_name,self.mother_name)
#     def print_daughter_name(self):
#         print(self.daughter_name)
# g=daughter('john','jaya','siya')
# g.print_parent_name()
# g.print_daughter_name()


# class C(object):
#     def __init__(self):
#         self.c=21
#         self.__d=15
# class D(C):
#     def __init__(self):
#         self.e=65
#         C.__init__(self)
# object1=D()
# print(object1.__d)

# def add (x,y,z=0):
#     return x+y+z
# print(add(2,3))
# print(add(3,5,7))

# class India:
#     def capital(self):
#         print('New delhi is the capital of India')
#     def  language(self):
#         print('Hindi is the most widely spoken language of India')
#     def type(self):
#         print('India is a developing country')
# class USA:
#     def capital(self):
#         print('Washington,D.C is the capital of USA')
#     def language(self):
#         print('English is the primary language of USA')
#     def type(self):
#         print('USA is a developed country')
# obj_ind=India()
# # obj_usa=USA()
# for country in (obj_ind,obj_usa):
#     country.capital()
#     country.language()
#     country.type()

# class Bird:
#     def intro(self):
#         print('There are many type of birds')
#     def flight(self):
#         print('most of the birds can fly but some cannot')
# class Sparrow(Bird):
#     def flight(self):
#         print('Sparrows can fly')
# class Ostrich(Bird):
#     def flight(self):
#         print('Ostrich cannot fly')
# obj_bird=Bird()
# obj_spr=Sparrow()
# obj_ost=Ostrich()
# obj_bird.intro()
# obj_bird.flight()
# obj_spr.intro()
# obj_spr.flight()
# obj_ost.intro()
# obj_ost.flight()

# class India:
#     def capital(self):
#         print('New delhi is the capital of India')
#     def  language(self):
#         print('Hindi is the most widely spoken language of India')
#     def type(self):
#         print('India is a developing country')
# class USA:
#     def capital(self):
#         print('Washington,D.C is the capital of USA')
#     def language(self):
#         print('English is the primary language of USA')
#     def type(self):
#         print('USA is a developed country')
# def func(obj):
#     obj.capital()
#     obj.language()
#     obj.type()
# obj_ind=India()
# obj_usa=USA()
# func(obj_ind)
# func(obj_usa)

# mytuple=('apple','banana','cherry')
# myit=iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))

# mystr='banana'
# myit=iter(mystr)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

# mytuple=('apple','banana','cherry')
# for x in mytuple:
#     print(x)

# class Mynumbers:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         x=self.a
#         self.a+=1
#         return x
# myclass=Mynumbers()
# myiter=iter(myclass)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# def greeting():
#     print('Hi!')
#     yield 1
#     print('How are you?')
#     yield 2
#     print('Are you there ?')
#     yield 3
# messenger=greeting(
# result=next(messenger)
# result=next(messenger)
# result=next(messenger)


# class rectangle:
#    def __init__(self,length,width):
#        self.length=length
#        self.width=width
#    def get_area(self):
#         area=self.length* self.width
#         print('Area of the rectangle=',area)
#    def get_perimeter(self):
#        perimeter=2*(self.length+self.width)
#        print('Perimeter of the rectangle=',perimeter)
# obj=rectangle(3,2)
# obj.get_perimeter()
# obj.get_area()



# class BankAccount:
#     def __init__(self,account_number,balance):
#         self.account_number=account_number
#         self.balance=balance
#     def deposit(self,amount):
#         self.deposit=amount
#     def withdraw(self,amount):
#         self.withdraw=amount
#     def get_balance(self):
#         Total=self.balance+self.deposit-self.withdraw
#         print('balance=',self.balance)
#         print('deposit=',self.deposit)
#         print('withdraw=',self.withdraw)
#         print('Total Balance=',Total)
# obj=BankAccount(12345678,1000)
# obj.deposit(2000)
# obj.withdraw(300)
# obj.get_balance()

# class Cars:
#     def __init__(self,make,model,year,colour):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.colour=colour
#     def get_make(self):
#         return
#     def get_model(self):
#         return
#     def get_year(self):
#        return
#     def colour(self):
#         return
#     def set_make(self,make1):
#         self.make=make1
#     def set_colour(self,colour2):
#         self.colour=colour2
# obj= Cars(make='BMW',model='2nd series',year=2000,colour='red')
# print(obj.make)
# print(obj.model)
# print(obj.year)
# print(obj.colour)
# obj.set_make('Suzuki')
# print(obj.make)
# obj.set_colour('yellow')
# print(obj.colour)

# class Animal:
#     def __init__(self,name,sound):
#         self.name=name
#         self.sound=sound
#     def speak(self):
#         return self.sound
# class Dog(Animal):
#     def __init__(self,name,sound,breed):
#         Animal.__init__(self,name,sound)
#         self.breed=breed
#     def get_breed(self):
#         return self.breed
# obj=Dog('Tommy','Bow','lab')
# print(obj.sound)
# print(obj.get_breed())

# class shapes:
#     def __init__(self,colour):
#         self.colour=colour
#     def get_colour(self):
#         return self.colour
# class square(shapes):
#     def __init__(self,colour,side_length):
#         shapes.__init__(self,colour)
#         self.side_length=side_length
#     def get_area(self):
#         return self.side_length**2
# obj=square('red',3)
# print(obj.get_colour())
# print(obj.get_area())


# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def get_name(self):
#         return self.name
#     def get_age(self):
#         return self.age
# class Employee(Person):
#     def __init__(self,name,age,salary):
#         Person.__init__(self,name,age)
#         self.salary=salary
#     def get_salary(self):
#         return self.salary
# obj=Employee('Sam',18,2000.50)
# print(obj.get_name())
# print(obj.get_age())
# print(obj.get_salary())