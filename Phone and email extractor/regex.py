import re                             # regex module

phone = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)
email = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                 # username
    @                                 # symbol
    [a-zA-Z0-9.-]+                    # domain name
    (\.[a-zA-Z]{2,4})                 # dot-something
       )''', re.VERBOSE)

output = open('log.txt','w')          # redirecting the output

input_file = open('file.txt').read()

for i in email.findall(input_file):
    print(i[0])
for f in phone.findall(input_file):
    print(f[0])
