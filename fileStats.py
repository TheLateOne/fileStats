import string

def fileStats(inputFile,outputFile):
	countLines, countWords, countNumbers, countPunct, countChars = 0, 0, 0, 0, 0
	for line in inputFile.readlines():
		countLines += 1
		for word in line.split(" "):
			countWords += 1
		for letter in line:
			countChars += 1
			if letter in string.digits:
				countNumbers += 1
			if letter in string.punctuation:
				countPunct += 1
		
	outputFile.write("Characters:{}\nWords:{}\nLines:{}\nDigits:{}\nPunctuation:{}\n".format(countChars, countWords, countLines, countNumbers,  countPunct))

fileStats(open("textinput.txt"), open("textoutput.txt","a"))