# date_changer.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY

import os
import re
import shutil
datePattern = re.compile(r'''^(.*?) # all text before the date
              ((0|1)?\d)-           # one or two digits for the month
              (.*?)$                # one or two digits for the day
              ((0|1|2|3)?\d)-       # four digits for the year
              ((19|20)\d\d)         # all text after the date
              ''',re.VERBOSE)

for american_file in os.listdir('.'):
    date = datePattern.search(american_file)
    # Skip the file without date
    if date == None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    abs_working_dir = os.path.abspath('.')
    amer = os.path.join(abs_working_dir,american_file)
    euro = os.path.join(abs_working_dir,euroFilename)
    #  rename the file
    shutil.move(amer,euro)
