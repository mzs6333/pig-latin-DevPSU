#This program converts a user input string into Pig Latin

message = input("Input your message to be converted to Pig Latin:\n")

vowels = "aeiouy"

def appAy(word):
	return word+'ay'

def findVowelInWord(word):
	index = 0
	for i in range(len(word)):
		if word[i] in vowels:
			index = i
			break
	return index
	
def rearrangeWord(word,index):
	firstFew = word[0:index]
	word = word[index:len(word)]
	word = word+firstFew
	return appAy(word)
	
wordList = message.split(' ')
finalWordString = ""

for i in range(len(wordList)):
	index = findVowelInWord(wordList[i])
	wordList[i] = rearrangeWord(wordList[i],index)
	finalWordString = finalWordString+wordList[i]+" "

print(finalWordString)