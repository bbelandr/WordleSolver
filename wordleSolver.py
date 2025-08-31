#!/usr/bin/env python3

import re

def findGreenLetter(letter, position):
    length = 4 - position
    goodWords = re.search(f"(\w{position}){letter}(\w{length})", goodWords)

def findYellowLetter(letter, position):
    length = 4 - position
    goodWords = re.search(f"")

def removeBlackLetter(letter, position):


introString = """\n\n\n\n\n\n\n\n\n\n\n

██╗    ██╗ ██████╗ ██████╗ ██████╗ ██╗     ███████╗
██║    ██║██╔═══██╗██╔══██╗██╔══██╗██║     ██╔════╝
██║ █╗ ██║██║   ██║██████╔╝██║  ██║██║     █████╗  
██║███╗██║██║   ██║██╔══██╗██║  ██║██║     ██╔══╝  
╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████╗███████╗
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝
                                                   
███████╗ ██████╗ ██╗    ██╗   ██╗███████╗██████╗   
██╔════╝██╔═══██╗██║    ██║   ██║██╔════╝██╔══██╗  
███████╗██║   ██║██║    ██║   ██║█████╗  ██████╔╝  
╚════██║██║   ██║██║    ╚██╗ ██╔╝██╔══╝  ██╔══██╗  
███████║╚██████╔╝███████╗╚████╔╝ ███████╗██║  ██║  
╚══════╝ ╚═════╝ ╚══════╝ ╚═══╝  ╚══════╝╚═╝  ╚═╝  
"""
print(introString)
goodWords = open("wordleWords")
for line in goodWords:
    print(goodWords.read())
    


