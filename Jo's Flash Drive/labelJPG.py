# This is a little script to lable the picture in the folder with number starting from 0.
# Author: Your dear boyfriend/coding genius.

def renameJPG(folderDir):
	labelNumber = 0
	import os
	for file in os.listdir(folderDir):
		if file.endswith(".jpg"):
			oldDir = folderDir+"/"+file
			newDir = folderDir+"/"+str(labelNumber)+".jpg"
			os.rename(oldDir, newDir)
			labelNumber +=1

if __name__ == "__main__":
	import sys
	folderDir = sys.argv[1]
	try:
		renameJPG(folderDir)
		print "Program Succeed"
	except:
		print "Program Fail"

		