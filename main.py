#61 lines, 200 characters

import os
import string
import random
import time

randomStuff = string.ascii_letters + string.digits + string.punctuation

def genRandom(lineStart = 0, characterStart = 0):
    randomOutput = ""
    for i in range(lineStart, 61):
        if i is lineStart:
            for x in range(characterStart, 199):
                randomOutput += random.choice(randomStuff)
        else:
            for x in range(0, 200):
                randomOutput += random.choice(randomStuff)
        randomOutput += "\n"
    return randomOutput

def addToLogo():
    lineNumber = 0
    characterNumber = 0
    file = open('banner.txt', 'r')

    toPrint = ""

    while True:
        randomness = genRandom(lineNumber, characterNumber)
        char = file.read(1)
        if '\n' in char:
            lineNumber += 1
            characterNumber = 0
        else:
            characterNumber += 1
        toPrint += char
        time.sleep(0.1)
        os.system("clear")
#        print(toPrint)
        print(toPrint + randomness)

        if lineNumber is 61 and characterNumber is 200:
            break

addToLogo()
