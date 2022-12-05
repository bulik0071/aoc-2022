import re
def importpuzzles(filename):
    file=open(filename)
    crates = []
    moves=[]
    replacingSign='$'
    for i, line in enumerate(file):
        if i<=7:
            crates.append(line.replace(' ',replacingSign).strip())
        if i > 9:
            auxillaryVar=[int(s) for s in re.findall(r'\b\d+\b', line.strip())]
            auxillaryVar[1]=auxillaryVar[1]-1
            auxillaryVar[2]=auxillaryVar[2]-1
            moves.append(auxillaryVar)
    crates=crates[::-1]
    indexes=[]
    for crate in crates:
        i=0
        for letter in crate:
            if letter.isalpha():
                indexes.append(i)
            i=i+1
        break
    auxCrates=['','','','','','','','','']
    for crate in crates:
        for letterindex,letter in enumerate(crate):
            for indexsingleindex, singleindex in enumerate(indexes):
                if singleindex==letterindex:
                    if letter!=replacingSign:
                        auxCrates[indexsingleindex]=auxCrates[indexsingleindex]+letter
    for auxCrate in auxCrates:
        auxCrate=list(map(str,auxCrate))
    crates=auxCrates
    return crates,moves
def moveCrateCrateMover9000(cratesQuantity,takeFrom, putTo):
    for x in range(0,cratesQuantity):
        letterToMove=takeFrom[-1]
        putTo=putTo+letterToMove
        takeFrom=takeFrom[:-1]
    return takeFrom,putTo
def moveCrateCrateMover9001(cratesQuantity,takeFrom, putTo):
    lettersToMove=takeFrom[-cratesQuantity:]
    putTo=putTo+lettersToMove
    takeFrom=takeFrom[:-cratesQuantity]
    return takeFrom,putTo
filename='puzzleinput.txt'
crates9000,moves9000=importpuzzles(filename)
crates9001,moves9001=importpuzzles(filename)
for move in moves9000:
    crates9000[move[1]],crates9000[move[2]]=moveCrateCrateMover9000(move[0],crates9000[move[1]],crates9000[move[2]])
    crates9001[move[1]],crates9001[move[2]]=moveCrateCrateMover9001(move[0],crates9001[move[1]],crates9001[move[2]])
outputString9000=''
outputString9001=''
for crate in crates9000: 
    outputString9000=outputString9000+crate[-1]
for crate in crates9001: 
    outputString9001=outputString9001+crate[-1]
print(f"Answer part 1: {outputString9000}")
print(f"Answer part 2: {outputString9001}")