# i = 0
#
# while i<4:
#     i+=1
#     print(i)
#     continue

# i = 0
# a = 'loops in python'
# print(len(a))
# while i < len(a):
#     if a[i] == 'o' or a[i] == 's':
#         i += 1
#         break
#     print(a[i])
#     i += 1
#
# i=0
# while i<4:
#     i+=1
#     print(i)
#     continue

# i=0
# a='loops in python'
# while i<len(a):
#     if a[i]=='o' or a[i]=='s':
#         i+=1
#         continue
#     print('current letter:',a[i])
#     i+=1

# i=0
# a='loops in python'
# while i<len(a):
#     if a[i]=='i' or a[i]=='s':
#         i+=2
#         break
#     print('current letter:',a[i])
#     i+=2

# a='loop in python'
# i=0
# while i<len(a):
#     i+=2
#     print(i)
# print('value of i:',i)
# print(len(a))

# i=0
# while i<4:
#     i+=1
#     print(i)
# else:
#     print('no break/n')

# i=0
# while i<4:
#     i+=1
#     print(i)
#     break
# else:
#     print('no break/n')

# print('list iteration')
# l=['hello','for','python']
# for i in l:
#     print(i)

# print('tuple iteration\n')
# t=('hello','for','python')
# for i in t:
#     print(i)

# print('\ndictionary iteration')
# d=dict()
# d['xyz']=123
# d['abc']=345
# for i in d:
#     print('%s %d'%(i,d[i]))

# for x in 'python developer':
#     if x=='e' or x=='o':
#         continue
#     print('current letter:', x)

# for x in 'python developer':
#     if x=='e' or x=='o':
#         break
#     print('current letter:',x)

# for x in 'python developer':
#     pass
# print('last letter:',x)
# #
# for i in range(10):
#     print(i,end='')
#     print()

# l=[10,20,30,40]
# for i in range(len(l)):
#     print(l[i],end=' ')
# print()

# sum=0
# for i in range(1,11):
#     sum=sum+i
# print('sum of first 10 natural number:',sum)

# for i in range(1,8):
#     print(i)
# else:
#     print('no break/n')

# adj=['red','big','tasty']
# fruits=['apple','banana','cherry']
# for x in adj:
#     for y in fruits:
#         print(x,y)

# upper_count=0
# lower_count=0
# text=input('enter text')
# for x in text:
#     if x.isupper():
#         upper_count+=1
#     elif x.islower():
#         lower_count+=1
# print(upper_count)
# print(lower_count)
# d=dict()
# d['lowercase']=lower_count
# d['uppercase']=upper_count
# print(d)
#

# number_of_vowel=0
# text=input('string : ')
# # for x in text:
# #     if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
# #         number_of_vowel+=1
# # print(number_of_vowel)
#
# vowel = ['a','e','i','o','u']
# for x in text:
#     if x.lower() in vowel:
#         number_of_vowel+=1
# print(number_of_vowel)
#
# sum=0
# for i in range (1,21,2):
#     sum=sum+i
#     print(i)
# print('sum of numbers:',sum )

#
# password='user'
# number_of_attempts=1
# text=input('enter password:')
# while number_of_attempts<3:
#     if text!='user':
#         print('try again')
#         print(f'You reached {number_of_attempts} out of 3 attempts')
#         number_of_attempts += 1
#         text = input('enter password')
#     else:
#         print('password is correct')
#         break



# password='user'
# number_of_attempts=1
# text=input('enter password:')
# while text:
#     if number_of_attempts < 3:
#         if text!=password:
#             print('try again')
#             print(f'You reached {number_of_attempts} out of 3 attempts')
#             number_of_attempts += 1
#             text = input('enter password')
#         elif text == password:
#             print('password is correct')
#             break
#     else:
#         print('You reached maximum number of attempts')
#         break

# movies=[
#     {'title':'inception',
#      'industry':'hollywood',
#      'year':2010},
#     {'title':'Zindagi Na Milega Dobara',
#      'industry':'bollywood',
#      'year':2011},
#     {'title':'The Avengers',
#      'industry':'hollywood',
#      'year':2012},
#     {'title':'Bajrangi Bhaijan',
#      'industry':'bollywood',
#      'year':2015},
#     {'title':'Parasite',
#      'industry':'korean',
#      'year':2019}]
# for x in movies:
#     for i in x:
#         if x[i]=='hollywood' and  x['year']>2010:
#                 print(x['title'])
#









