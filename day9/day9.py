
puzzles='puzzleinput.txt'
rawPuzzles = open(puzzles).read().strip()
lines = [x for x in rawPuzzles.split('\n')]

def adjustRope(HEAD,TAIL):
    row = (HEAD[0]-TAIL[0])
    column = (HEAD[1]-TAIL[1])
    if abs(row)<=1 and abs(column)<=1:
        pass
    elif abs(row)>=2 and abs(column)>=2:
        TAIL = (HEAD[0]-1 if TAIL[0]<HEAD[0] else HEAD[0]+1, HEAD[1]-1 if TAIL[1]<HEAD[1] else HEAD[1]+1)
    elif abs(row)>=2:
        TAIL = (HEAD[0]-1 if TAIL[0]<HEAD[0] else HEAD[0]+1, HEAD[1])
    elif abs(column)>=2:
        TAIL = (HEAD[0], HEAD[1]-1 if TAIL[1]<HEAD[1] else HEAD[1]+1)
    return TAIL

HEAD = (0,0)
TAIL = [(0,0) for _ in range(9)]
ROWDIRECTION = {'L': 0, 'U': -1, 'R': 0, 'D': 1}
COLUMNDIRECTION = {'L': -1, 'U': 0, 'R': 1, 'D': 0}
PART1 = set([TAIL[0]])
PART2 = set([TAIL[8]])
for line in lines:
    direction,stepsno = line.split()
    stepsno = int(stepsno)
    for _ in range(stepsno):
        HEAD = (HEAD[0] + ROWDIRECTION[direction], HEAD[1]+COLUMNDIRECTION[direction])
        TAIL[0] = adjustRope(HEAD, TAIL[0])
        for i in range(1, 9):
            TAIL[i] = adjustRope(TAIL[i-1], TAIL[i])
        PART1.add(TAIL[0])
        PART2.add(TAIL[8])
print(len(PART1))
print(len(PART2))