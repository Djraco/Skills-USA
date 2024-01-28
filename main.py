import math
import sys
from tkinter import filedialog as fd

def sign(x): #sign function. Helps with the creativity^2 rule.
    return (x > 0) - (x < 0)

def checkList(input, method): #handles all errors regarding the traits lists

    if type(input) is not list:
        print(method + "Error: Expected list. Got " + str(type(input)))
        sys.exit()
    
    if len(input) != 4:
        print(method + "Error: Expected 4 intergers. Got " + str(len(input)))
        sys.exit()

    for i, v in enumerate(input):
        if v is not int:
            print(method + "Error: all scores/traits must be an interger from 0-9.")
            sys.exit()


def addTrait(traits): #returns the base profile rounded to the hundredths place.
    personality = traits[0]
    creativity = traits[1]
    detail = traits[2]
    teamWork = traits[3]

    baseProfile = math.sqrt(abs(
        2 * personality + 
        sign(creativity) * pow(creativity, 2) + 
        2 * detail + 
        (3 * teamWork - creativity)
        ))

    return round(baseProfile, 2)

def subTrait(traits): #subtracts 5 from each trait and returns the modified list.
    for i, v in enumerate(traits):
        traits[i] = v-5

    return traits

def getFile(): #display an 'open file' dialogue
    filename = fd.askopenfilename()
    return(filename)

def statusTrait():
    return

#main method




scores = [5, 6, 4, 5]

scores = subTrait(scores)
baseProfile = addTrait(scores)

print(baseProfile)
getFile()