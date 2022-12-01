"""Day 1: Calorie Counting"""
import re
f = open('puzzleinput.txt')
rawpuzzleinput=list(f)
elvesCalories={}
top={}
elfIndex=1
actualCalories=0
top3Value=0
for x in rawpuzzleinput:
        try:
            actualCalories=actualCalories+int(re.search(r'\d+', x).group())
        except AttributeError:
            elvesCalories['Elf no:'+str(elfIndex)]=actualCalories
            actualCalories=0
            elfIndex=elfIndex+1
elvesCalories['Elf no: '+str(elfIndex)]=actualCalories
maxValue=max(elvesCalories.values())
elfCarryingMostCalories=max(elvesCalories,key=elvesCalories.get)
print(f"Answer: {elfCarryingMostCalories} is carrying {maxValue} calories in total")
for x in range(0,3):
    maxValue=max(elvesCalories.values())
    elfCarryingMostCalories=max(elvesCalories,key=elvesCalories.get)
    top['Top '+str(x+1)]=maxValue
    top3Value=top3Value+maxValue
    del elvesCalories[elfCarryingMostCalories]
print(f"Answer: Top 3 elves are carrying {top3Value} calories in total")


