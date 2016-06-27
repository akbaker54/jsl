# At any rate, right now this should work with all the 1B drills--and you can easily expand that list.

import os
import sys


def frst(x):
    (first, second, third, fourth, fifth) = x
    return first


def ffrst(x):
    (first,second) = x
    return first


def scnd(x):
    (first, second, third, fourth, fifth) = x
    return second


def sscnd(x):
    (first,second) = x
    return second


def thrd(x):
    (first, second, third, fourth, fifth) = x
    return third


def frth(x):
    (first, second, third, fourth, fifth) = x
    return fourth


def ffth(x):
    (first, second, third, fourth, fifth) = x
    return fifth


def frstScnd(x):
    return (frst(x), scnd(x))


def listTotxt(yourlist, txtname):
    # assert type(txtname)=='str'
    file_obj = open(txtname, "w")
    for line in yourlist:
        file_obj.write(line + "\n")


def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)


drillCheck = {'1A.A': False, '1A.B': False, '1A.C': False, '1A.D': False, '1A.E': False, '1A.F': False, '1A.G': False, '1A.H': False, '1A.I': False, '1A.J': False, '1B.A': False, '1B.B': False, '1B.C': False, '1B.D': False, '1B.E': False, '1B.F': False, '1B.G': False, '1B.H': False, '1B.I': False, '1B.J': False, '1B.K': False, '2A.A': False, '2A.B': False, '2A.C': False, '2A.D': False, '2A.E': False, '2A.F': False, '2A.G': False, '2A.H': False, '2B.A': False, '2B.B': False, '2B.C': False, '2B.D': False, '2B.E': False, '2B.F': False, '2B.G': False, '2B.H': False, '2B.I': False, '2B.J': False, '2B.K': False, '3A.A': False, '3A.B': False, '3A.C': False, '3A.D': False, '3A.E': False, '3A.F': False, '3A.G': False, '3A.H': False, '3A.I': False, '3A.J': False, '3B.A': False, '3B.B': False, '3B.C': False, '3B.D': False, '3B.E': False, '3B.F': False, '3B.G': False, '3B.H': False, '3B.I': False, '3B.J': False, '4A.A': False, '4A.B': False, '4A.C': False, '4A.D': False, '4A.E': False, '4A.F': False, '4A.G': False, '4A.H': False, '4A.I': False, '4A.J': False, '4A.K': False, '4A.L': False, '4A.M': False, '4A.N': False, '4A.O': False, '4A.P': False, '4A.Q': False, '4A.R': False, '4A.S': False, '4A.T': False, '4A.U': False, '4B.A': False, '4B.B': False, '4B.C': False, '4B.D': False, '4B.E': False, '4B.F': False, '4B.G': False, '4B.H': False, '4B.I': False, '4B.J': False, '4B.K': False, '4B.L': False, '5A.A': False, '5A.B': False, '5A.C': False, '5A.D': False, '5A.E': False, '5A.F': False, '5A.G': False, '5A.H': False, '5A.I': False, '5A.J': False, '5A.K': False, '5A.L': False, '5A.M': False, '5A.N': False, '5A.O': False, '5B.A': False, '5B.B': False, '5B.C': False, '5B.D': False, '5B.E': False, '5B.F': False, '5B.G': False, '5B.H': False, '5B.I': False, '5B.J': False, '5B.K': False, '5B.L': False, '5B.M': False, '6A.A': False, '6A.B': False, '6A.C': False, '6A.D': False, '6A.E': False, '6A.F': False, '6A.G': False, '6A.H': False, '6A.I': False, '6A.J': False, '6A.K': False, '6A.L': False, '6A.M': False, '6A.N': False, '6A.O': False, '6B.A': False, '6B.B': False, '6B.C': False, '6B.D': False, '6B.E': False, '6B.F': False, '6B.G': False, '6B.H': False, '6B.I': False, '6B.J': False, '6B.K': False, '6B.L': False, '7A.A': False, '7A.B': False, '7A.C': False, '7A.D': False, '7A.E': False, '7A.F': False, '7A.G': False, '7A.H': False, '7A.I': False, '7A.J': False, '7A.K': False, '7A.L': False, '7A.M': False, '7A.N': False, '7B.A': False, '7B.B': False, '7B.C': False, '7B.D': False, '7B.E': False, '7B.F': False, '7B.G': False, '7B.H': False, '7B.I': False, '7B.J': False, '7B.K': False, '7B.L': False, '7B.M': False, '7B.N': False, '7B.O': False, '7B.P': False, '7B.Q': False, '7B.R': False, '8A.A': False, '8A.B': False, '8A.C': False, '8A.D': False, '8A.E': False, '8A.F': False, '8A.G': False, '8A.H': False, '8A.I': False, '8A.J': False, '8A.K': False, '8A.L': False, '8A.M': False, '8A.N': False, '8B.A': False, '8B.B': False, '8B.C': False, '8B.D': False, '8B.E': False, '8B.F': False, '8B.G': False, '8B.H': False, '8B.I': False, '8B.J': False, '8B.K': False, '8B.L': False, '8B.M': False, '8B.N': False, '9A.A': False, '9A.B': False, '9A.C': False, '9A.D': False, '9A.E': False, '9A.F': False, '9A.G': False, '9A.H': False, '9A.I': False, '9A.J': False, '9A.K': False, '9A.L': False, '9A.M': False, '9B.A': False, '9B.B': False, '9B.C': False, '9B.D': False, '9B.E': False, '9B.F': False, '9B.G': False, '9B.H': False, '9B.I': False, '9B.J': False, '9B.K': False, '9B.L': False, '9B.M': False, '9B.N': False, '9B.O': False, '9B.P': False, '9B.Q': False, '10A.A': False, '10A.B': False, '10A.C': False, '10A.D': False, '10A.E': False, '10A.F': False, '10A.G': False, '10A.H': False, '10A.I': False, '10A.J': False, '10A.K': False, '10A.L': False, '10A.M': False, '10A.N': False, '10A.O': False, '10A.P': False, '10A.Q': False, '10A.R': False, '10A.S': False, '10B.A': False, '10B.B': False, '10B.C': False, '10B.D': False, '10B.E': False, '10B.F': False, '10B.G': False, '10B.H': False, '10B.I': False, '10B.J': False, '10B.K': False, '10B.L': False, '10B.M': False, '10B.N': False, '11A.A': False, '11A.B': False, '11A.C': False, '11A.D': False, '11A.E': False, '11A.F': False, '11A.G': False, '11A.H': False, '11A.I': False, '11A.J': False, '11A.K': False, '11A.L': False, '11A.M': False, '11A.N': False, '11A.O': False, '11A.P': False, '11A.Q': False, '11B.A': False, '11B.B': False, '11B.C': False, '11B.D': False, '11B.E': False, '11B.F': False, '11B.G': False, '11B.H': False, '11B.I': False, '11B.J': False, '11B.K': False, '11B.L': False, '12A.A': False, '12A.B': False, '12A.C': False, '12A.D': False, '12A.E': False, '12A.F': False, '12A.G': False, '12A.H': False, '12A.I': False, '12A.J': False, '12A.K': False, '12A.L': False, '12A.M': False, '12A.N': False, '12A.O': False, '12A.P': False, '12A.Q': False, '12B.A': False, '12B.B': False, '12B.C': False, '12B.D': False, '12B.E': False, '12B.F': False, '12B.G': False, '12B.H': False, '12B.I': False, '12B.J': False, '12B.K': False, '12B.L': False, '12B.M': False, '12B.N': False}


'because'
printToFile = True

drillInfo2A = {1: (2, 'A', 'A', 2, 9), 2: (2, 'A', 'B', 2, 8), 3: (2, 'A', 'C', 2, 8), 4: (2, 'A', 'D', 2, 8),
               5: (2, 'A', 'E', 2, 8), 6: (2, 'A', 'F', 2, 8), 7: (2, 'A', 'G', 2, 8), 8: (2, 'A', 'H', 2, 8)}

drillInfo2B = {1: (2, 'B', 'A', 2, 14), 2: (2, 'B', 'B', 2, 9), 3: (2, 'B', 'C', 2, 9), 4: (2, 'B', 'D', 2, 6),
               5: (2, 'B', 'E', 2, 8), 6: (2, 'B', 'F', 2, 12), 7: (2, 'B', 'G', 2, 9), 8: (2, 'B', 'H', 2, 9),
               9: (2, 'B', 'I', 2, 10), 10: (2, 'B', 'J', 2, 10), 11: (2, 'B', 'K', 2, 9)}

drillInfo3A = {1: (3, 'A', 'A', 2, 8), 2: (3, 'A', 'B', 2, 10), 3: (3, 'A', 'C', 2, 7), 4: (3, 'A', 'D', 2, 6),
               5: (3, 'A', 'E', 2, 10), 6: (3, 'A', 'F', 2, 10), 7: (3, 'A', 'G', 2, 6), 8: (3, 'A', 'H', 2, 7),
               9: (3, 'A', 'I', 2, 6), 10: (3, 'A', 'J', 2, 6)}

drillInfo3B = {1: (3, 'B', 'A', 2, 6), 2: (3, 'B', 'B', 2, 7), 3: (3, 'B', 'C', 2, 7), 4: (3, 'B', 'D', 2, 9),
               5: (3, 'B', 'E', 2, 9), 6: (3, 'B', 'F', 2, 6), 7: (3, 'B', 'G', 2, 6), 8: (3, 'B', 'H', 2, 7),
               9: (3, 'B', 'I', 2, 8), 10: (3, 'B', 'J', 2, 12)}

drillInfo4A = {1: (4, 'A', 'A', 2, 6), 2: (4, 'A', 'B', 2, 6), 3: (4, 'A', 'C', 2, 6), 4: (4, 'A', 'D', 2, 5),
               5: (4, 'A', 'E', 2, 7), 6: (4, 'A', 'F', 2, 6), 7: (4, 'A', 'G', 2, 7), 8: (4, 'A', 'H', 2, 8),
               9: (4, 'A', 'I', 2, 7), 10: (4, 'A', 'J', 2, 5), 11: (4, 'A', 'K', 2, 6), 12: (4, 'A', 'L', 2, 6),
               13: (4, 'A', 'M', 2, 7), 14: (4, 'A', 'N', 2, 6), 15: (4, 'A', 'O', 2, 6), 16: (4, 'A', 'P', 4, 7),
               17: (4, 'A', 'Q', 2, 8), 18: (4, 'A', 'R', 2, 12), 19: (4, 'A', 'S', 2, 7), 20: (4, 'A', 'T', 2, 8),
               21: (4, 'A', 'U', 2, 5)}

drillInfo4B = {1: (4, 'B', 'A', 2, 9), 2: (4, 'B', 'B', 2, 5), 3: (4, 'B', 'C', 2, 8), 4: (4, 'B', 'D', 2, 7),
               5: (4, 'B', 'E', 2, 7), 6: (4, 'B', 'F', 2, 6), 7: (4, 'B', 'G', 2, 6), 8: (4, 'B', 'H', 2, 6),
               9: (4, 'B', 'I', 2, 6), 10: (4, 'B', 'J', 2, 8), 11: (4, 'B', 'K', 2, 6), 12: (4, 'B', 'L', 2, 8)}

drillInfo = {1: (drillInfo2A, "2A"), 2: (drillInfo2B, "2B"), 3: (drillInfo3A, "3A"), 4: (drillInfo3B, "3B"),
             5: (drillInfo4A, "4A"), 6: (drillInfo4B, "4B")}

adict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

# probs have a for loop over a bunch of files,

for k in range(1, len(drillInfo) + 1):
    drillList = []
    section = sscnd(drillInfo[k])
    sectionDrillInfo = ffrst(drillInfo[k])
    ensure_dir("/JSL/" + section)
    print(os.listdir("/JSL/"))
    for j in range(1, len(sectionDrillInfo) + 1):
        drillNum = thrd(sectionDrillInfo[j])
        sectionDrill = section + ".Dr." + drillNum
        numu = frth(sectionDrillInfo[j])
        numex = ffth(sectionDrillInfo[j])
        numint = numu * numex + numex + 1
        #    print(numint)
        labelList = []
        count = 0
        for i in range(1, numint):
            utt = i % (numu + 1)
            #        print(utt, "\t", i)
            if utt == 0:
                utt = numu + 1
            if utt == 1:
                labelList.append("")
                count += 1
            else:
                #            print("{}.{}.{}{}".format(section, drillNum, count, adict[utt-1]))
                labelList.append("{}.{}.{}{}".format(section, drillNum, count, adict[utt - 1]))
        # print(labelList)
        if printToFile:
            ensure_dir("/JSL/" + section + "/" + sectionDrill)
            listTotxt(labelList, "JSL" + '/' + section + '/' + sectionDrill + '/' + sectionDrill + '.txt')
        drillCheck[k-1]
        drillList.append(sectionDrill)
    if printToFile:
        listTotxt(drillList, "JSL" + "/" + section + "/" + section + 'drill list.txt')
