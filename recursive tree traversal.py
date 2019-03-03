import os

def MoveDown(filePath):
	directories = os.listdir(filePath)
	if ".DS_Store" in directories:
		directories.remove(".DS_Store")

	if len(directories) == 0:
		with open ("%s/checked.txt" %filePath,'w') as f:
			f.write("checked for viruses")
	elif len(directories) >= 1:
		for i in directories:
			newPath = filePath + "/" + i
			MoveDown(newPath)
		with open ("%s/checked.txt" %filePath,'w') as f:
			f.write("checked for viruses")

def DeleteChecks(filePath):
	directories = os.listdir(filePath)
	if ".DS_Store" in directories:
		directories.remove(".DS_Store")
	if "checked.txt" in directories:
		directories.remove("checked.txt")

	if len(directories) == 0:
		os.remove("%s/checked.txt" %filePath)
	elif len(directories) >= 1:
		for i in directories:
			newPath = filePath + "/" + i
			DeleteChecks(newPath)
		os.remove("%s/checked.txt" %filePath)

def SmallTest(filePath):
	directories = os.listdir(filePath)
	print(directories)
	if ".DS_Store" in directories:
		directories.remove(".DS_Store")
	print(directories)
	# with open ("%s/checked.txt" %filePath,'w') as f:
	# 		f.write("small tested")
