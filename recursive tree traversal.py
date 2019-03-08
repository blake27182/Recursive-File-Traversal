import os

def MoveDown(filePath):				# Recursive function that explores each branch of the file structure
	directories = os.listdir(filePath)	# Stores the immediate children of the current folder in directories
	if ".DS_Store" in directories:		# Removes the apple-specific hidden file if it exists
		directories.remove(".DS_Store")

	if len(directories) == 0:		# Base case: if the function is run in a leaf, the folder is "checked"
		with open ("%s/checked.txt" %filePath,'w') as f:
			f.write("checked for viruses")
	elif len(directories) >= 1:		# Recursive case: the function is run again in each of the child directories
		for i in directories:
			newPath = filePath + "/" + i
			MoveDown(newPath)
		with open ("%s/checked.txt" %filePath,'w') as f:	# When all children have been explored, "check" the 
			f.write("checked for viruses")			# 	current folder and go out of scope into the 
									#	previous recursion
def DeleteChecks(filePath):		# Recursive function that deletes files created by the MoveDown function
	directories = os.listdir(filePath)	# Stores the immediate children of the current folder in directories
	if ".DS_Store" in directories:		# Removes the apple-specific hidden file if it exists
		directories.remove(".DS_Store")
	if "checked.txt" in directories:	# Removes the "checked" file if it exists from directories
		directories.remove("checked.txt")

	if len(directories) == 0:		# Base case: if the function is run in a leaf, delete the "checked" file
		os.remove("%s/checked.txt" %filePath)
	elif len(directories) >= 1:		# Recursive case: the function is run again in each of the child directories
		for i in directories:
			newPath = filePath + "/" + i
			DeleteChecks(newPath)
		os.remove("%s/checked.txt" %filePath)		# After all children have been explored, delete the "checked"
								#	file and move out of scope into previous recursion
def SmallTest(filePath):		# Test function to test different methods used in the recursive functions
	directories = os.listdir(filePath)
	print(directories)
	if ".DS_Store" in directories:
		directories.remove(".DS_Store")
	print(directories)
	# with open ("%s/checked.txt" %filePath,'w') as f:
	# 		f.write("small tested")
