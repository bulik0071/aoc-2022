def importpuzzles(filename):
    file=open(filename)
    rawpuzzleinput=list(file)
    return rawpuzzleinput
def checkdatastream(inputString,datalength):
    startMarker=0
    inputString=list(map(str,inputString))
    for letterIndex,letter in enumerate(inputString):
        substringArray=[]
        for x in range(0,datalength):
            substringArray.append(inputString[letterIndex+x])
        if len(substringArray) != len(set(substringArray)):
            pass
        else:
            startMarker=letterIndex+datalength
            break
    return startMarker
filename='puzzleinput.txt'
datalengthp1=4
datalengthp2=14
print(f'Answer for part 1: {checkdatastream(importpuzzles(filename)[0],datalengthp1)}')
print(f'Answer for part 2: {checkdatastream(importpuzzles(filename)[0],datalengthp2)}')