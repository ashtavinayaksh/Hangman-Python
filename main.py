from random import randint


def getWord():
     nWord = randint(0, 279486)
     with open("Words.txt", "r") as f:
          allWords = f.readlines()
          global word
          word = allWords[nWord]
     word = word[:-1]
     
     
     i = 0
     underscore = ""
     while i < len(word):
          underscore = underscore + "_ "
          i += 1
     print("\nThe word is " + str(len(word)) + " characters long:\n" + underscore + "\n")

getWord()

def guessLetter():
     guessedLetter = input("Guess a letter: ").upper()

     letters = []
     for char in word:
          letters.append(char)

     if guessedLetter in letters:
          print(guessedLetter, "is correct!")

     else:
          print("Try again.")
          print(word, letters)
          guessLetter()


guessLetter()