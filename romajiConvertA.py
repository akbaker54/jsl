import sys
import os

roomazib = input("Modified JSL means you should use 'N' for syllabic n and 'G' for nasal g. Additionally, use square brackets to indicate hight tone.")

roomazi = ""
for char in roomazib:
    if char == "[" or "]":
        break
    roomazi.append(char)
syl = ""
y == False
vowel = False
sylDone = False
for char in roomazi.split():
    lens = len(syl)
#    if char = "N":
#        syl.append("n̄")
#        sylDone = True
#    if char = "G":
#        syl.append('ḡ')
    if char in ['a','i','u','e','o']:
        vowel == True
    elif char = 'y':
        y == True
    if lens == 0:
        if vowel == True:
            syl.append(char)
            sylDone = True
    if lens == 1:
        syl.append(char)
        if vowel = False:
            output.append('q')
    if lens == 2:
        assert syl[1] = 'y'
        syl.append(char)
        sylDone = True
    if sylDone == True:
        output.append('syl')
        syl = ''
    y == False
    vowel == False
    
while i in range(0,len(roomazi-1)):
    if 