#########################################################
#       TSC Lunch                                       #
#       ---------                                       #
#       Split names signed up into 5 groups,            #
#       Then randomly select an order for them.         #
#       Uses previous results to ensure fairness.       #
#                                                       #
#       See README at:                                  #
#       https://github.com/MattyAyOh/TSCLunch           #
#########################################################

import datetime
import glob
import os
import random
import Tkinter

####################################################
# Change this for number of minutes between groups #
####################################################
minutesBetweenGroups = 8
####################################################

def loadResponses():
        responsesFile = None
        try:
                newest = max(glob.iglob('CSVResponses/*.csv'), key=os.path.getctime)
                responsesFile = open(newest,'r')
        except ValueError:
                print "Failure!  No CSV files found in CSVResponses folder.  Exiting script..."
        return responsesFile

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
        
def generateNameRanges(responsesFile):
        listOfFirstNames = []
        listOfLastNames = []

        for line in responsesFile:
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
        dictOfNameRangeIndexes = {"f1":0,"f2":1,"f3":2,"f4":3,"f5":4,"l1":5,"l2":6,"l3":7,"l4":8,"l5":9}
        firstNameRanges = ['f1','f2','f3','f4','f5']
        lastNameRanges = ['l1','l2','l3','l4','l5']
        
        dictPR = loadPreviousResults()
        firstorlast = 2
        if( dictPR['first']-dictPR['last'] >= 3 ):
                firstorlast = 1
        if( dictPR['last']-dictPR['first'] >= 3 ):
                firstorlast = 0
        if( firstorlast == 2 ):
                firstorlast = random.choice([0,1])

        if firstorlast == 0:
                dictPR['first']+=1
                
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

                writeToResultsFileWithDict(dictPR)

                finalListIndexes = []
                for nameRange in newSortedNameRanges:
                        finalListIndexes.append(dictOfNameRangeIndexes[nameRange])

                return [firstorlast, finalListIndexes]

        if firstorlast == 1:
                dictPR['last']+=1
                
                lastNameRangeValues = [dictPR['l1'], dictPR['l2'], dictPR['l3'], dictPR['l4'], dictPR['l5']]
                lowestValue = min(lastNameRangeValues)
                highestSelected = 0
                lowestNameRanges = []
                for nameRange in lastNameRanges:
                        if dictPR[nameRange] == lowestValue:
                                lowestNameRanges.append(nameRange)

                newSortedNameRanges = []
                newSortedNameRanges.append(random.choice(lowestNameRanges))
                lastNameRanges.remove(newSortedNameRanges[-1])

                while( len(lastNameRanges) > 0 ):
                        newSortedNameRanges.append(random.choice(lastNameRanges))
                        lastNameRanges.remove(newSortedNameRanges[-1])

                pointsToAdd = 4
                for nameRange in newSortedNameRanges:
                        dictPR[nameRange]+=pointsToAdd
                        pointsToAdd-=1

                writeToResultsFileWithDict(dictPR)

                finalListIndexes = []
                for nameRange in newSortedNameRanges:
                        finalListIndexes.append(dictOfNameRangeIndexes[nameRange])

                return [firstorlast, finalListIndexes]


        
def sortNRListByIList( taggedDict, indexList ):
        finalSortedList = []
        for index in indexList:
                finalSortedList.append(taggedDict[index])
        return finalSortedList

def quit(root):
    root.destroy()
    
def formatNameRanges( listNameRanges, FoL ):
        longestNameStart = 0
        longestNameEnd = 0
        for pair in listNameRanges:
                if len(pair[0]) > longestNameStart:
                        longestNameStart = len(pair[0])
                if len(pair[1]) > longestNameEnd:
                        longestNameEnd = len(pair[1])

        widestTableLength = (longestNameStart + 3 + longestNameEnd)
        headerSpacing = (widestTableLength/2)-4
        
        if FoL == 0:
                headerString = "First Names:"
        elif FoL == 1:
                headerString = "Last Names:"
                headerSpacing -= 1
                

        
        t = datetime.datetime.now()
        finalString = ""
        for i in range(headerSpacing):
                finalString += " "
        finalString += "%s\n" % (headerString)
        for i in range(widestTableLength+1):
                finalString += "-"
        finalString += "\n"
        for pair in listNameRanges:
                time = t.strftime("%H:%M")
                finalString += "%*s - %-*s -> %s\n" % (longestNameStart, pair[0], longestNameEnd, pair[1],time)
                t = t + datetime.timedelta(0,(60*minutesBetweenGroups))

        print finalString
        print "Script Finished, First paste into an E-mail;"
        print "Then Press Ctrl+C to close script"
        r = Tkinter.Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(finalString)
        r.mainloop()
        r.quit()


def main():
        respFile = loadResponses()
        if(not(respFile)):
                return
        if(not(os.path.isfile("PreviousResults.txt"))):
                dictionaryBlankResultsSheet = {"first":0,"last":0,"f1":0,"f2":0,"f3":0,"f4":0,"f5":0,"l1":0,"l2":0,"l3":0,"l4":0,"l5":0}
                writeToResultsFileWithDict( dictionaryBlankResultsSheet )

        allNameRanges = generateNameRanges(respFile)
        taggedNameRanges = tagNameRanges(allNameRanges)
        firstOrLastAndListIndexes = pickNameRange()
        firstOrLast = firstOrLastAndListIndexes[0]
        listIndexes = firstOrLastAndListIndexes[1]
        finalList = sortNRListByIList(taggedNameRanges, listIndexes)
        formatNameRanges(finalList, firstOrLast)

if __name__ == "__main__":
    main()
