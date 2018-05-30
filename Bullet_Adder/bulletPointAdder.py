#! python3
import sys
import pyperclip # send and receive text form computer clipboard

text = pyperclip.paste()
if text  == None:
    print('Please copy the list to add Bullets')
lines = text.split('\n')
for i in  range (len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)
print('Bullets added to the list')
