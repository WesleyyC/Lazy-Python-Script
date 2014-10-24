# This is a little script update the README.md file according to the current status of the folder
# Author: Your dear boyfriend/coding genius.

# import module
import os

# update places we have been
def updatePlace():
	places = []

	for filename in os.listdir("."):
		if os.path.isdir(os.path.join(os.path.abspath("."), filename)):
			places.append(filename)
	
	result = "# We have been to: " + places[0]

	for i in range(1,len(places)-1):
		result += ", " + places[i]

	result += " and " + places[len(places)-1]

	return result + "\n"

# update the date
def updateDate():
	import time
	return "# Date: " + time.strftime("%m/%d/%Y") + "\n"

# update the total number
def updateTotalNumber():
	totalNumber = 0
	for stuff in os.listdir("."):
		potentialDir = os.path.join(os.path.abspath("."), stuff)
		if os.path.isdir(potentialDir):
			for filename in os.listdir(potentialDir):
				if filename.endswith(".jpg"):
					totalNumber += 1
	return "# Photos In Total: "+ str(totalNumber) + "\n"

# change a specific line
def replaceLine(line_num, text):
    lines = open("README.md", 'r').readlines()
    lines[line_num] = text
    out = open("README.md", 'w')
    out.writelines(lines)
    out.close()

# update the file
def updateFile(updatePlaceStr, updateTotalNumberStr, updateDateStr):
	replaceLine(1,updatePlaceStr)
	replaceLine(2,updateTotalNumberStr)
	replaceLine(3,updateDateStr)

# main method
def updateREADME():
	updatePlaceStr = updatePlace() 
	updateTotalNumberStr = updateTotalNumber()
	updateDateStr = updateDate()
	updateFile(updatePlaceStr, updateTotalNumberStr, updateDateStr)

if __name__ == "__main__":
	updateREADME()

	