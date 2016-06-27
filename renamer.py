import os
import sys


def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]


#print listdir_fullpath('JSL')
dirs = ['JSL']
wavFiles = {}
for thing in dirs:
    print "Searching through ", thing, "..."
    fullPath = listdir_fullpath(thing)
    for i in range(0,len(fullPath)):
        item = fullPath[i]
        local = os.listdir(thing)[i]
        if os.path.isdir(item):
            print item,"is a directory"
            dirs.append(fullPath[i])
        elif item.endswith(".wav"):
            wavFiles[fullPath[i]] = local
            print item,"is a .wav"
        else:
            print item, "is something else."
    print "Done with ", thing, "!"
drFiles = {}
for key in wavFiles.keys():
    if 'CC' not in key:
        drFiles[key] = wavFiles[key]
    else:
        print "\tnot", item    

for key in drFiles:
    item = drFiles[key]
    if item.find("2") != -1:
        insert = item.find("2") + 2
        front = item[0:insert]
        end = item[insert:]
        print front + ".Dr" + end
    else:
        print item
#dirs = os.listdir('JSL')
#        
#for item in dirs:
#    if item.endswith(".wav") and 'CC' not in item:
#        insert = item.find("2") + 2
#        front = item[0:insert]
#        end = item[insert:]
#        print front + ".Dr" + end
#    elif item.find(".") == -1:
#        item.append
#    else:
#        print "\t","not",item
        