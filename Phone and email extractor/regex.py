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
matches = []
for groups in phone.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    print(phoneNum,file = output)

for group in email.findall(text):
     print(group[0],file = output)

if len(matches) > 0:
    print('Copied to log.txt')
else:
    print('No phone numbers or email addresses found.')
