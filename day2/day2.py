"""--- Day 2: Rock Paper Scissors ---"""
import re
f = open('puzzleinput.txt')
rawpuzzleinput=list(f)
result=[]
choosePoints=0
gamePoints=0  
totalPoints=0
wins=0 
draws=0 
loses=0
choosePoints_1=0
gamePoints_1=0
totalPoints_1=0
wins_1=0
draws_1=0
loses_1=0
for singleGame in rawpuzzleinput:
    result.append(re.sub('\n', '', singleGame).split(' '))
for singleResult in result:
    if singleResult[0]=='C' and singleResult[1] =='X' or singleResult[0]=='A' and singleResult[1] =='Y' or singleResult[0]=='B' and singleResult[1] =='Z':
        gamePoints=gamePoints+6
        wins=wins+1
    elif singleResult[0]=='A' and singleResult[1] =='X' or singleResult[0]=='B' and singleResult[1] =='Y' or singleResult[0]=='C' and singleResult[1] =='Z':
        gamePoints=gamePoints+3
        draws=draws+1
    else:
        gamePoints=gamePoints
        loses=loses+1
    if singleResult[1]=='X':
        choosePoints=choosePoints+1
    elif singleResult[1]=='Y':
        choosePoints=choosePoints+2
    elif singleResult[1]=='Z':
        choosePoints=choosePoints+3
totalPoints=choosePoints+gamePoints
for singleResult in result:
    if singleResult[0]=='B' and singleResult[1] =='Z' or singleResult[0]=='C' and singleResult[1] =='Y' or singleResult[0]=='A' and singleResult[1] =='X':
        choosePoints_1=choosePoints_1+3
    elif singleResult[0]=='A' and singleResult[1] =='Z' or singleResult[0]=='B' and singleResult[1] =='Y' or singleResult[0]=='C' and singleResult[1] =='X':
        choosePoints_1=choosePoints_1+2
    else:
        choosePoints_1=choosePoints_1+1
    if singleResult[1]=='Z':
        gamePoints_1=gamePoints_1+6
        wins_1=wins_1+1
    elif singleResult[1]=='Y':
        gamePoints_1=gamePoints_1+3
        draws_1=draws_1+1
    elif singleResult[1]=='X':
        loses_1=loses_1+1
totalPoints_1=choosePoints_1+gamePoints_1
print(f'Part1: Choose points: {choosePoints}, game points: {gamePoints}. Total points: {totalPoints}. Wins: {wins}, draws: {draws}, loses: {loses}')
print(f'Part1: Choose points: {choosePoints_1}, game points: {gamePoints_1}. Total points: {totalPoints_1}. Wins: {wins_1}, draws: {draws_1}, loses: {loses_1}')