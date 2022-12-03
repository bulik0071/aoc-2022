"""--- Day 3: Rucksack Reorganization ---"""
import string
import re
"""===============================PART1==============================================="""
priorityDataSet=list(string.ascii_lowercase)+list(string.ascii_uppercase)
repeatedLettersinRucksacks=[]
sumofpriorities=0
filename='puzzleinput.txt'
def importpuzzles(filename):
    file=open(filename)
    rawpuzzleinput=list(file)
    allRucksacks=[]
    for singleRucksack in rawpuzzleinput:
        allRucksacks.append(re.sub('\n', '', singleRucksack).split(' '))
    return allRucksacks
def checkforrepeatsinstring(inputString):
    listedStringPart1=[]
    listedStringPart2=[]
    repeatedLetter=''
    i=0
    stringLength=len(inputString)
    for letter in inputString:
        if i<stringLength/2:
            listedStringPart1.append(letter)
        else:
            listedStringPart2.append(letter)
        i=i+1
    for firstLetter in listedStringPart1:
        for secondLetter in listedStringPart2:
            if firstLetter==secondLetter:
                repeatedLetter=firstLetter
    return repeatedLetter#, listedStringPart1, listedStringPart2,stringLength
def createprioritydataset(inputString):
    j=0
    priorityDict={}
    for letter in priorityDataSet:
        j=j+1
        priorityDict[str(letter)]=j
    return priorityDict
priorityDict=createprioritydataset(priorityDataSet)
allRucksacks=importpuzzles(filename)
k=0
for singleRuckSack in allRucksacks:
    repeatedLettersinRucksacks.append(checkforrepeatsinstring(singleRuckSack[0]))
for letter in repeatedLettersinRucksacks:
    sumofpriorities=sumofpriorities+priorityDict[letter]
print(f'Sum of priorities part 1 : {sumofpriorities}')
"""===============================PART2==============================================="""
badges=[]
sumofbadgespriorities=0
def checkfortriplerepeat(inputString_0,inputString_1,inputString_2):
    repeatedLetter=''
    for firstLetter in inputString_0:
        for secondLetter in inputString_1:
            for thirdLetter in inputString_2:
                if firstLetter==secondLetter and secondLetter==thirdLetter:
                    repeatedLetter=firstLetter
    return repeatedLetter
for singleRuckSack in range(0,len(allRucksacks),3):
    badges.append(checkfortriplerepeat(allRucksacks[singleRuckSack][0],allRucksacks[singleRuckSack+1][0],allRucksacks[singleRuckSack+2][0]))    
for letter in badges:
    sumofbadgespriorities=sumofbadgespriorities+priorityDict[letter]
print(f'Sum of priorities part 2 : {sumofbadgespriorities}')


