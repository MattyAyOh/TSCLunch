import datetime

#Change this for number of minutes between groups
minutesBetweenGroups = 8
#################################################
f = open('lunch.csv', 'r')
listOfFirstNames = []
listOfLastNames = []
for line in f:
	name = line.split(',')[1]
	try:
		listOfFirstNames.append(name.split(' ')[0].title().rstrip())
		listOfLastNames.append(name.split(' ')[1].title().rstrip())
	except IndexError:
		listOfFirstNames.append(name.title()[0].rstrip())

listOfFirstNames = sorted(listOfFirstNames[1:-1])
listOfLastNames = sorted(listOfLastNames[1:-1])

lastSplit = len(listOfLastNames)/5
firstSplit = len(listOfFirstNames)/5

firstFinishedList = []
lastFinishedList = []
for i in range(5):
	firstSplitList = listOfFirstNames[i*firstSplit:(i+1)*firstSplit]
	firstFinishedList.append([firstSplitList[0],firstSplitList[-1]])
	lastSplitList = listOfLastNames[i*lastSplit:(i+1)*lastSplit]
	lastFinishedList.append([lastSplitList[0],lastSplitList[-1]])

	if i == 4:
		firstFinishedList[-1][1] = listOfFirstNames[-1]
		lastFinishedList[-1][1] = listOfLastNames[-1]

longestFirstName = 0
longestFirstName2 = 0
for pair in firstFinishedList:
	if len(pair[0]) > longestFirstName:
		longestFirstName = len(pair[0])
	if len(pair[1]) > longestFirstName2:
		longestFirstName2 = len(pair[1])

t = datetime.datetime.now()
print
print "First Names:"
for pair in firstFinishedList:
	time = t.strftime("%H:%M")
	print "%*s - %-*s -> %s" % (longestFirstName, pair[0], longestFirstName2, pair[1],time)
	t = t + datetime.timedelta(0,(60*minutesBetweenGroups))


longestLastName = 0
longestLastName2 = 0
for pair in lastFinishedList:
	if len(pair[0]) > longestLastName:
		longestLastName = len(pair[0])
	if len(pair[1]) > longestLastName2:
		longestLastName2 = len(pair[1])

print
t = datetime.datetime.now()
print "Last Names:"
for pair in lastFinishedList:
	time = t.strftime("%H:%M")
	print "%*s - %-*s -> %s" % (longestLastName, pair[0], longestLastName2, pair[1],time)
	t = t + datetime.timedelta(0,(60*minutesBetweenGroups))

print
