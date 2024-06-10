# import re
# txt='The rain in Spain'
# x=re.search('^The .*Spain$',txt)
# print(x)
# if x:
#     print('Yes we have a match!')
# else:
#     print('No match')


# import re
# txt='The rain in Spain'
# x=re.findall('ai',txt)
# print(x)

# import re
# txt='The rain in Spain'
# x=re.findall('Portugal',txt)
# print(x)
# if x:
#     print('Yes atleast we have one match')
# else:
#     print("No match!")


# import re
# txt='The rain in Spain'
# x=re.search('\s',txt)
# print('The first white space character is located in position :',x.start())
# print(x)

# import re
# txt='The rain in Spain'
# x=re.search('Portugal',txt)
# print(x)

# import re
# txt='The rain in Spain'
# x=re.split('\s',txt)
# print(x)
#
# import re
# txt='The rain in Spain'
# x=re.split('\s',txt,2)
# print(x)
#
# import re
# txt='The rain in Spain'
# x=re.sub('\s','_',txt)
# print(x)

# import re
# txt='The rain in Spain'
# x=re.sub('\s','9',txt,2)
# print(x)

# import re
# txt='The rain in Spain'
# x=re.search('ai',txt)
# print(x)

# import re
# txt='The rain in Spain'
# x=re.search(r'\bS\w+',txt)
# print(x.span())


# import re
# txt='The rain in Spain'
# x=re.search(r'\bS\w+',txt)
# print(x.group())

# import re
# txt='The rain in Spain'
# x=re.search(r'\bS\w+',txt)
# print(x.string)

import re
# # print(re.search(r'^x','xenon'))
# print(re.search(r's$','geeks'))
# print((re.search(r'a.','rain')))
# print(re.search(r'9','45998'))
# print(re.search(r'9+','45998'))
# print(re.search(r'\d{3}','hello1234'))
# print(re.search(r'\s','xenon is agas'))
# print(re.search(r'\D+\d*','123 greek 123'))
# print(re.search(r'[^abc]','abcde'))
# print(re.search('[a-p]','xenon'))
# print(re.search(r'(?:AB)',"ABCDE"))
# x=re.search(r'(\w*),(\w*)','best,day')
# print(x.group(1))
# print(x.group(2))
# print(x.groups())

# print(re.search(r'and','Sun And Moon',flags=re.IGNORECASE))

# exp=('''Hello there
# It is
# A nice day''')
# print(re.findall(r'^\w',exp,flags=re.MULTILINE))


import re
txt = ('My name is Vipin. vipinkc.ipcs@gmail.com is my official mail id.'
       'My personal mail id is kcvipin@gmail.com. +91 9876543210 is my phone number')

# mail = re.findall(r'[\w\.]+@[\w.]+[^\.\s]',txt)

mail = re.findall(r'[\w.]+@[\w.]+[^\.\s]',txt)

print(mail)

num = re.findall(r'\+\d{2}\s\d{10}',txt)
print(num)