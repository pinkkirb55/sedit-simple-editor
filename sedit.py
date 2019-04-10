from sys import argv
import os
from os.path import exists

clearCommand = 'clear'
script, toEdit = argv
helpFile = 'seditHelp.txt'
lineNum = 1
inputData = ""
writeData = []
 
if os.name == 'nt':
	clearCommand = 'cls'

os.system(f'{clearCommand}')


if exists(toEdit) == True:
	print(f"File {toEdit} exists.")
else:
	print(f"File {toEdit} does not exist, creating...")

print("Press 'h' to print help file.")
while True:
	consoleCommand = input(":")
	
	if 'h' in consoleCommand.lower():
		fle = open(helpFile)
		print(fle.read())
	if 'l' in consoleCommand.lower():
		fle = open(toEdit, 'r+')
		print(fle.read())
	
	if 'n' in consoleCommand.lower():
		print(f"Opening {toEdit} in NEW mode.")
		fle = open(toEdit, 'w')
		while inputData != ' ':
			inputData = input("\t" + "\033[33;2;2m" + f"{lineNum}" + "\t" + "\033[0;0;0m")
			lineNum += 1
			writeData.append(inputData + '\n')
			fle.writelines(writeData)
			writeData = []
	
	if 'i' in consoleCommand.lower():
		consoleCommand.split(' ')
		print(f"Opening {toEdit} in APPEND/EDIT mode")
		fle = open(toEdit, 'r+')
		writeData = fle.readlines()
		try:
			writeData[(int(consoleCommand[2]) - 1)] = input("\t" + "\033[33;2;2m" + f"{consoleCommand[2]}" + "\t" + "\033[0;0;0m") + '\n'
			fle.truncate(0)
			fle.writelines(writeData)
		except IndexError:
			print("The line you're trying to insert in doesn't exist.\n")
	
	if 'd' in consoleCommand.lower():
		consoleCommand.split('-')
		print(f"DELETE MODE")
		fle = open(toEdit, 'r+')
		writeData = fle.readlines()
		try:
			writeData.pop((int(consoleCommand[2]) - 1))
			fle.truncate(0)
			fle.writelines(writeData)
		except IndexError:
			print("The line you're trying to delete doesn't exist.\n")		
	
	if 'q' in consoleCommand.lower():
		break
		
fle.close()

