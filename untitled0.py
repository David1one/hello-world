# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 22:26:23 2020

@author: David McMahon
"""

#Run in the correct git repository
BOT_FILENAME = "test.txt"
COMMIT_MESSAGE = "AFSD"
#TEXT = """Hi there,
#    We were trying to float README directory to top.
#    Don't change this file, our bot is constantly doing so!"""

TEXT="WHA..."

EXTRA_CHAR = "!"

import sys
import os

res = False
if os.path.exists(BOT_FILENAME):
    with open(BOT_FILENAME, "r+") as f:
        if f.read() == TEXT:
            res = True

with open(BOT_FILENAME, "w+") as f:
    if res:
        f.write(TEXT+EXTRA_CHAR)
    else:
        f.write(TEXT)

#os.system('git add test.txt & git commit -m "test" & git push -f')

os.system()
#os.system("git add " + BOT_FILENAME)
#os.system('git commit -m "'+COMMIT_MESSAGE+'" --author="Droid-bot <574nemobot@gmail.com>"')
#os.system('git push -f')

#git commit --author="John Doe <john@doe.org>"