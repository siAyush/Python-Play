'''
mcb.py - Saves and loads pieces of text to the clipboard.
Usage: mcb.py save <keyword> - Saves clipboard to keyword.
       mcb.py <keyword> - Loads keyword to clipboard.
       mcb.py list - Loads all keywords to clipboard.
       mcb.py delete <keyword> - delete the keyword.
       mcb.py delete - delete all the keywords.
'''

import shelve
import pyperclip
import sys

# Save clipboard content
mcb = shelve.open('data')
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb.keys())))

    elif sys.argv[1] in mcb:
        pyperclip.copy(mcb[sys.argv[1]])
mcb.close()

# delete keyword
if len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    mcb = shelve.open('data')
    del mcb[sys.argv[2]]
    mcb.close()

# delete all keywords
if len(sys.argv) == 2 and sys.argv[1].lower() == 'delete':
    mcb = shelve.open('data')
    for i in list(mcb.keys()):
        del mcb[i]
    mcb.close()
