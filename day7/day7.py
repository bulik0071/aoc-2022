from collections import defaultdict
def importpuzzles(filename):
    puzzles=open(filename).read()
    lines=[x for x in puzzles.split('\n')]
    return lines
filename='puzzleinput.txt'
lines=importpuzzles(filename)
MYDICT = defaultdict(int)
path = []
for line in lines:
    words = line.strip().split()
    if words[1] == 'cd':
        if words[2] == '..':
            path.pop()
        else:
            path.append(words[2])
    elif words[1] == 'ls':
        continue
    elif words[0] == 'dir':
        continue
    else:
        mydict = int(words[0])
        for i in range(1, len(path)+1):
            MYDICT['/'.join(path[:i])] += mydict
    print(path)
maximumUsed = 70000000 - 30000000
totalUsed = MYDICT['/']
needed = totalUsed - maximumUsed
ansP1 = 0
ansP2 = 1e9
for key,value in MYDICT.items():
    if value <= 100000:
        ansP1 += value
    if value>=needed:
        ansP2 = min(ansP2, value)
print(f"Answer for part 1: {ansP1}")
print(f"Answer for part 2: {ansP2}")