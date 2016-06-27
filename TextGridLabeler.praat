form Section
	comment What section and drill are you running this over? Make sure this sound and TextGrid are open.
	text section 1B.A
	comment What tier do you want labelled?
	integer tier 1
endform
stringlength = 0
filelength = 0
firstnewline = 0
oldlabel$ = ""
newlabel$ = ""
sect$ = "1B"
filename$ = "JSL/" + sect$ +"/"+section$+"/"+section$+".txt"
writeInfoLine: "help"
appendInfoLine: filename$

if fileReadable (filename$)
	file$ < 'filename$'
	leftoverlength = 0
	if file$ = ""
		exit The text file is empty.
	endif
	filelength = length (file$)
	leftover$ = file$
	numberOfIntervals = Get number of intervals... tier
	for interval from 1 to numberOfIntervals
		firstnewline = index (leftover$, newline$)
		newlabel$ = left$ (leftover$, (firstnewline - 1))
		leftoverlength = length (leftover$)
		leftover$ = right$ (leftover$, (leftoverlength - firstnewline))	
		Set interval text... tier interval 'newlabel$'
	endfor
else 
	exit The label text file 'filename$' does not exist where it should!
endif
