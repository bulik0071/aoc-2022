import re
filename='puzzleinput.txt'
def importpuzzles(filename):
    file=open(filename)
    rawpuzzleinput=list(file)
    lines=[]
    for line in rawpuzzleinput:
        lines.append(re.sub('\n', '', line).split(' '))
    return lines
def prepareLine(inputArray):
    outputArray=[]
    i=''
    for line in inputArray:
        i=line[0].replace('-','#').replace(',','#')
        outputArray.append(i.split('#'))
    return outputArray
def checkifcontains(inputArray):
    if int(inputArray[0])>=int(inputArray[2]) and int(inputArray[1])<=int(inputArray[3]) or int(inputArray[2])>=int(inputArray[0]) and int(inputArray[3])<=int(inputArray[1]):
        return True
    else:
        return False
def checkifoverlap(inputArray):
    if int(inputArray[0])>=int(inputArray[2]) and int(inputArray[0])<=int(inputArray[3]) or int(inputArray[1])>=int(inputArray[2]) and int(inputArray[1])<=int(inputArray[3]) or int(inputArray[2])>=int(inputArray[0]) and int(inputArray[2])<=int(inputArray[1]) or int(inputArray[3])>=int(inputArray[0]) and int(inputArray[3])<=int(inputArray[0]):
        return True
    else:
        return False
myArray=prepareLine(importpuzzles(filename))
assingments=0
overlaps=0
for element in myArray:
    if checkifcontains(element):
        assingments=assingments+1
    if checkifoverlap(element):
        overlaps=overlaps+1
print(f"Total assignments: {assingments}")
print(f"Total overlaps: {overlaps}")
