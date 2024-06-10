# a = 150
# b= 100
# if b>a:
#     print('b > a')
# elif b == a:
#     print('a = b')
# elif b < a:
#     print('b < a')
# else:
#     print('Else executed')

# age = int(input("Enter age here : "))
# id = input('Voter id? ')
# if age >= 18 and id == 'y':
#     print('Eligible for vote!')
# else:
#     print('Not eligible for vote!')
# a=150
# b=100
# if b>a:
#     print("b is geater than a")
# elif a==b:
#     print('a=b')
# else:
#     print("b<a")
# x=int(input())
# if x>10:
#     print('above 10')
#     if x>20:
#         print('and also above 20!')
#     else:
#         print('but not above 20')
# a=int(input("number"))
# # if a%2==0:
# #     print('a is even')
# # elif a%2!=0:
# #     print('a is odd')
# if a%7==0:
#     print('a is a multiple of 7')
# else:
#     print('not a multiple of 7')
# a=int(input("units"))
# price=0
# if 0<a<100:
#     print('no charge')
# elif a>100:
#     if a>200:
#         price=((a-200)*10)
#         print(price)
#         if a<200:
#             price+=(a-100)*5
#             print(price)

#
# u = int(input("enter : "))
# price = 0
# if u<100:
#     print("No charge")
# elif u>100:
#     if u<200:
#         price = (u-100)*5
#         print(price)
#     elif u>200:
#         price = 100*5
#         price += (u-200)*10
#         print(price)
# sample={
# 'a':'100',
# 'b':'200',
# # 'c':'300'
# # }
# # sample.pop('b')
# # print(sample)
# # a=int(input('number:'))
# # if a%5==0:
# #     print('hello')
# # elif a%5!=0:
# #     print('bye')
# a=int(input('age:'))
# if a>=18:
#     print('adult')
# elif 13<=a<=17:
#     print('teenager')
# elif a<13:
#     print('child')

# print(str(100))
# x=len(str(100))
# print(x)
# a=int(input('number:'))
# if len(str(a))==3:
#     print('3 digit')
# elif len(str(a))==2:
#     print('2 digit')
# elif len(str(a))==4:
#     print('4 digit')
# a=int(input('length:'))
# b=int(input('length:'))
# c=int(input('length:'))
# if a==b==c:
#     print('is an equilateral triangle')
# elif a==c or b==c or a==b:
#     print('is an isoscelles triangle ')
# else:
#     print('scalene triangle')


# age1=int(input('age 1:'))
# age2=int(input('age 2:'))
# age3=int(input('age 3:'))
# age4=int(input('age 4:'))
# if age1>=age2:
#     # print('youngest child=age 2')
#     youngest_child=age2
# if age2>=age3:
#     # print('youngest child=age 3')
#     youngest_child=age3
# if age3>=age4:
#     # print('youngest child=age 4')
#     youngest_child=age4
# if age1<=age2:
#     # print('youngest child=age 1')
#     youngest_child=age1
# print('Age ',youngest_child,'is the youngest child')



# age1=int(input('age 1:'))
# age2=int(input('age 2:'))
# age3=int(input('age 3:'))
# age4=int(input('age 4:'))
# if age1<(age2 or age3 or age4):
#     print('age1 is the youngest child')
# if age2<(age1 or age3 or age4):
#     print('youngest child=age2')
# if age3<(age1 or age2 or age4):
#     print('youngest child=age3')
# if age4<(age1 or age2 or age3):
#     print('youngest child=age4')