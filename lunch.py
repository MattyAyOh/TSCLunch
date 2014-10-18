import datetime
import glob
import os
import random


#################################################
#Change this for number of minutes between groups
#################################################
minutesBetweenGroups = 8
#################################################

try:
        newest = max(glob.iglob('CSVResponses/*.csv'), key=os.path.getctime)
except ValueError:
        print "Failure!  No CSV files found in CSVResponses folder.  Exiting script..."
f = open(newest,'r')

def generatePreviousResultsFile():
        resultsFile = open("PreviousResults.txt", "w")
        resultsFile.write("first:0\n")
        resultsFile.write("last:0\n")
        resultsFile.write("f1:0\n")
        resultsFile.write("f2:0\n")
        resultsFile.write("f3:0\n")
        resultsFile.write("f4:0\n")
        resultsFile.write("f5:0\n")
        resultsFile.write("l1:0\n")
        resultsFile.write("l2:0\n")
        resultsFile.write("l3:0\n")
        resultsFile.write("l4:0\n")
        resultsFile.write("l5:0\n")
        resultsFile.close()
        
def generateNameRanges():
        listOfFirstNames = []
        listOfLastNames = []

        for line in f:
                name = line.split(',')[1]
                try:
                        listOfFirstNames.append(name.split(' ')[0].title().rstrip())
                        listOfLastNames.append(name.split(' ')[1].title().rstrip())
                except IndexError:
                        listOfFirstNames.append(name.title().rstrip())

        listOfFirstNames = sorted(listOfFirstNames[1:-1])
        listOfLastNames = sorted(listOfLastNames[1:-1])

        firstSplitAmount = len(listOfFirstNames)/5
        lastSplitAmount = len(listOfLastNames)/5


        firstFinishedList = []
        lastFinishedList = []
        for i in range(5):
                firstSplitList = listOfFirstNames[i*firstSplitAmount:(i+1)*firstSplitAmount]
                firstFinishedList.append([firstSplitList[0],firstSplitList[-1]])
                lastSplitList = listOfLastNames[i*lastSplitAmount:(i+1)*lastSplitAmount]
                lastFinishedList.append([lastSplitList[0],lastSplitList[-1]])

                #If last name range, replace the end range name with the last name in the overall list
                if i == 4:
                        firstFinishedList[-1][1] = listOfFirstNames[-1]
                        lastFinishedList[-1][1] = listOfLastNames[-1]

        return firstFinishedList + lastFinishedList

def tagNameRanges( allNameList ):
        taggedNameRanges = {}
        for i, tempList in enumerate(allNameList):
                taggedNameRanges[i] = tempList

        return taggedNameRanges

def loadPreviousResults():
        dictPreviousResults = {}
        previousResults = open('PreviousResults.txt','r')
        for line in previousResults:
                dictPreviousResults[line.split(':')[0]]=int(line.split(':')[1])
        return dictPreviousResults

def pickNameRange():
        dictPR = loadPreviousResults()
        firstorlast = 2
        if( dictPR['first']-dictPR['last'] >= 2 ):
                firstorlast = 1
        if( dictPR['last']-dictPR['first'] >= 2 ):
                firstorlast = 0
        if( firstorlast == 2 ):
                firstorlast = random.choice([0,1])


        dictPR['first']+=1
        firstNameRanges = ['f1','f2','f3','f4','f5']
        firstNameRangeValues = [dictPR['f1'], dictPR['f2'], dictPR['f3'], dictPR['f4'], dictPR['f5']]
        lowestValue = min(firstNameRangeValues)
        highestSelected = 0
        lowestNameRanges = []
        for nameRange in firstNameRanges:
                if dictPR[nameRange] == lowestValue:
                        lowestNameRanges.append(nameRange)

        newSortedNameRanges = []
        newSortedNameRanges.append(random.choice(lowestNameRanges))
        firstNameRanges.remove(newSortedNameRanges[-1])

        while( len(firstNameRanges) > 0 ):
                newSortedNameRanges.append(random.choice(firstNameRanges))
                firstNameRanges.remove(newSortedNameRanges[-1])

        pointsToAdd = 4
        for nameRange in newSortedNameRanges:
                dictPR[nameRange]+=pointsToAdd
                pointsToAdd-=1
                


        dictOfNameRangeIndexes = {"f1":0,"f2":1,"f3":2,"f4":3,"f5":4,"l1":5,"l2":6,"l3":7,"l4":8,"l5":9}

        finalListIndexes = []
        for nameRange in newSortedNameRanges:
                finalListIndexes.append(dictOfNameRangeIndexes[nameRange])

        return finalListIndexes

def writeToResultsFileWithDict( dictNameRanges ):
        resultsFile = open("PreviousResults.txt", "w")
        resultsFile.write("first:%d\n" % (dictNameRanges["first"]))
        resultsFile.write("last:%d\n" % (dictNameRanges["last"]))
        resultsFile.write("f1:%d\n" % (dictNameRanges["f1"]))
        resultsFile.write("f2:%d\n" % (dictNameRanges["f2"]))
        resultsFile.write("f3:%d\n" % (dictNameRanges["f3"]))
        resultsFile.write("f4:%d\n" % (dictNameRanges["f4"]))
        resultsFile.write("f5:%d\n" % (dictNameRanges["f5"]))
        resultsFile.write("l1:%d\n" % (dictNameRanges["l1"]))
        resultsFile.write("l2:%d\n" % (dictNameRanges["l2"]))
        resultsFile.write("l3:%d\n" % (dictNameRanges["l3"]))
        resultsFile.write("l4:%d\n" % (dictNameRanges["l4"]))
        resultsFile.write("l5:%d\n" % (dictNameRanges["l5"]))
        resultsFile.close()
        
def sortNRListByIList( taggedDict, indexList ):
        finalSortedList = []
        for index in indexList:
                finalSortedList.append(taggedDict[index])
        return finalSortedList
                
def formatNameRanges( listNameRanges ):
        longestFirstName = 0
        longestFirstName2 = 0
        for pair in listNameRanges:
                if len(pair[0]) > longestFirstName:
                        longestFirstName = len(pair[0])
                if len(pair[1]) > longestFirstName2:
                        longestFirstName2 = len(pair[1])

        t = datetime.datetime.now()
        print "First Names:"
        for pair in listNameRanges:
                time = t.strftime("%H:%M")
                print "%*s - %-*s -> %s" % (longestFirstName, pair[0], longestFirstName2, pair[1],time)
                t = t + datetime.timedelta(0,(60*minutesBetweenGroups))


def main():
        if(not(os.path.isfile("PreviousResults.txt"))):
                generatePreviousResultsFile()
        allNameRanges = generateNameRanges()
        taggedNameRanges = tagNameRanges(allNameRanges)
        listIndexes = pickNameRange()
        finalList = sortNRListByIList(taggedNameRanges, listIndexes)
        formatNameRanges(finalList)

if __name__ == "__main__":
    main()
