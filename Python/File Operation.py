# file = open(r'C:\Users\USER\Downloads\narendra modi.txt','r')
# print(file.read(100))

# file=open(r'C:\Users\USER\Downloads\narendra modi.txt','r')
# for line in file:
#     print(line)

# file=open(r'C:\Users\USER\Downloads\narendra modi.txt','r')
# # print(file.read())
# print(file.read(8))

# file=open('heyy.txt','w')
# file.write('This is the write command' )
# file.write(' it allows us to write in a particular file')
# file.close()
# file=open('heyy.txt','r')
# print(file.read())


#
# file=open('My file.txt','w')
# L=['This is Delhi\n','This is Paris\n','This is London']
# file.writelines(L)
# file.close()
# file=open('My file.txt','a')
# file.write('\n')
# file.write('Today')
# file.write(' Tomarrow')
# file=open('My file.txt','r')
# print('Output of readlines are appending')
# print(file.read())

#
# L=['This is Delhi\n','This is Paris\n','This is London\n']
# with open('new.txt','w') as file1:
#     file1.write('Hello\n')
#     file1.writelines(L)
# with open('new.txt','a') as file1:
#     file1.write('Today')
# with open('new.txt','r+')as file1:
#     print(file1.read())

# a=[1,2,3]
# try:
#     print('Second element=%d,'%(a[1]))
#     print('Fourth element=%d,'%(a[3]))
# except:
#     print('An error occured')


# def fun(a):
#     if a<4:
#         b=a/(a-3)
#     print('Value of b=',b)
# try:
#     fun(3)
#     fun(5)
# except ZeroDivisionError:
#     print('Zero Divison Error occured and handled')
# except NameError:
#     print('Name Error occured and handled')


# def X(a,b):
#     try:
#         c=((a+b)/(a-b))
#     except ZeroDivisionError:
#         print('a/b results in 0')
#     else:
#         print(c)
# X(2,3)
# X(3,3)

# try:
#     k=5//0
#     print(k)
# except ZeroDivisionError:
#     print("Can't divide by zero")
# finally:
#     print('This is always executed')

# try:
#     raise NameError("Hi there")
# except NameError:
#     print('An exception')
#     raise

class Myerror(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return (repr(self.value))
try:
    raise (Myerror(3*2))
except Myerror as error:
    print('A new exception occured : ',error.value)
