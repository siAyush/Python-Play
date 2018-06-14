'''
How to use?
Just copy the file text and run this file regex.py and the output is
in the log.txt file which is created by this file.
'''
import re                             # regex module
import pyperclip


phone = re.compile(r'''(              # phone number regex
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    )''', re.VERBOSE)

email = re.compile(r'''(              # email regex
    [a-zA-Z0-9._%+-]+                 # username
    @                                 # symbol
    [a-zA-Z0-9.-]+                    # domain name
    (\.[a-zA-Z]{2,4})                 # dot-something
       )''', re.VERBOSE)

output = open('log.txt','w')          # redirecting the output

text = str(pyperclip.paste())
for groups in phone.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    print(phoneNum,file = output)

for group in email.findall(text):
     print(group[0],file = output)
