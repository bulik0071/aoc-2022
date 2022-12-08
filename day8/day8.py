import numpy as np
def importpuzzles(filename):
    puzzles=open(filename).read()
    lines_1=[x for x in puzzles.split('\n')]
    lines=[]
    for row in lines_1:
        singleLine=[]
        for letter in row:
            singleLine.append(letter)
        lines.append(singleLine)
    return lines
filename='puzzleinput.txt'
puzzles=importpuzzles(filename)
viewFromLeft=np.array(puzzles)
viewFromUp=viewFromLeft.transpose()
viewFromBottom=np.flip(viewFromUp,-1)
viewFromRight=np.flip(viewFromLeft,-1)
def makeVisibilityMask(inputArray):
    visibilityArray=[]
    for line in inputArray:
        treeMaxValue=0
        visibilityLine=[]
        for treeindex, tree in enumerate(line):
            if treeindex==0 and int(tree)==0:
                visibilityLine.append(1)
            else:
                if int(tree)>treeMaxValue:
                    visibilityLine.append(1)
                    treeMaxValue=int(tree)
                else:
                    visibilityLine.append(0)
        visibilityArray.append(visibilityLine)
    return visibilityArray
def eachTreeVisibility(inputArray):
    visibilityArray=[]
    for line in inputArray:
        lineVisibility=[]
        for indextree,tree in enumerate(line):
            treeVisibility=0
            for x in range(indextree,len(line)):
                if x!=indextree:
                    if int(tree)>int(line[x]):
                        treeVisibility+=1
                    elif int(tree)<=int(line[x]):
                        treeVisibility+=1
                        break
            lineVisibility.append(treeVisibility)
        visibilityArray.append(lineVisibility)    
    return visibilityArray
maskFromLeft=np.array(makeVisibilityMask(viewFromLeft))
maskFromRight=np.flip(np.array(makeVisibilityMask(viewFromRight)),-1)
maskFromUp=np.array(makeVisibilityMask(viewFromUp)).transpose()
maskFromBottom=np.flip(np.array(makeVisibilityMask(viewFromBottom)),-1).transpose()
eachTreemaskFromLeft=np.array(eachTreeVisibility(viewFromLeft))
eachTreemaskFromRight=np.flip(np.array(eachTreeVisibility(viewFromRight)),-1)
eachTreemaskFromUp=np.array(eachTreeVisibility(viewFromUp)).transpose()
eachTreemaskFromBottom=np.flip(np.array(eachTreeVisibility(viewFromBottom)),-1).transpose()
treesTotal=0
for indexLine, lineofTree in enumerate(maskFromLeft):
    for indexTree,tree in enumerate(lineofTree):
        if maskFromLeft[indexTree][indexLine]==1 or maskFromRight[indexTree][indexLine]==1 or maskFromBottom[indexTree][indexLine]==1 or maskFromUp[indexTree][indexLine]==1:
            treesTotal+=1
maxMul=0
for indexLine, lineofTree in enumerate(maskFromLeft):
    for indexTree,tree in enumerate(lineofTree):
        auxVar=eachTreemaskFromLeft[indexTree][indexLine]*eachTreemaskFromRight[indexTree][indexLine]*eachTreemaskFromUp[indexTree][indexLine]*eachTreemaskFromBottom[indexTree][indexLine]
        if auxVar>maxMul:
            maxMul=auxVar
print(f'Part1 answer: {treesTotal}')
print(f'Part2 answer: {maxMul}')