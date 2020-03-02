word = raw_input("Type a word   ")
wordList = list(word.lower())
updatedSpaces = []
wordLen = len(word)
lives = 5
letter = " "
x = 0
letterIndex = 0
letterIndex2 = 0
letterIndex3 = 0
inWord = False
inWord2 = False
inWord3 = False

for i in range(0,100):
    print(" ")

for i in range (0, int(wordLen)):
    updatedSpaces.append("_")
    
print(updatedSpaces)

def getLetter():
    global letter
    letter = raw_input ("Enter a letter guess    ")

def check():
    global updatedSpaces
    global lives
    global letter
    global x
    global letterIndex
    global letterIndex2
    global letterIndex3
    global inWord
    global inWord2
    global inWord3

    while updatedSpaces != wordList:
        for i in range(0, int(wordLen)):
            if letter == wordList[i]:
                letterIndex = i
                inWord = True
                break
            else:
                inWord = False
        for i in range(0, int(wordLen)):
            if (letter == wordList[i]) and (i != letterIndex):
                letterIndex2 = i
                inWord2 = True
                break
            else:
                inWord2 = False 
        for i in range(0, int(wordLen)):
            if (letter == wordList[i]) and (i != letterIndex) and (i != letterIndex2):
                letterIndex3 = i
                inWord3 = True
                break
            else:
                inWord3 = False 
        if inWord:
            updatedSpaces[letterIndex] = wordList[letterIndex]
            checklist = "".join(updatedSpaces)
            master = "".join(wordList)
            if checklist == master:
                print("Congrats you solved the word!    ")
                break
        if inWord2:
            updatedSpaces[letterIndex2] = wordList[letterIndex2]
            checklist = "".join(updatedSpaces)
            master = "".join(wordList)
            if checklist == master:
                print("Congrats you solved the word!    ")
                break
        if inWord3:
            updatedSpaces[letterIndex3] = wordList[letterIndex3]
            checklist = "".join(updatedSpaces)
            master = "".join(wordList)
            if checklist == master:
                print("Congrats you solved the word!    ")
                break
        if (inWord == False) and (inWord2 == False):
            lives -= 1
            if lives == 0:
                print("Game Over   ")
                break
        print(updatedSpaces)
        print("You have: " + str(lives) + " lives left!")
        getLetter()
        x += 1
    
    
    
      
                
def game():
    getLetter()
    check()
    
game()                      