#HANGMAN GAME
import random

words = ["apple","orange","banana"]
chosen_word = random.choice(words)

print("The secret word is: ", chosen_word)

#printing blanks
guessed_word=[]
for i in range(0,len(chosen_word)):
    guessed_word.append("_")
 


lives = 3
while guessed_word!=list(chosen_word) and lives>0 : # convert chosen word to list for list comparison 
    guessed_letter = input("Enter a letter: ")
    guessed_letter = guessed_letter.lower()
    
    if guessed_letter in chosen_word:
        for i,char in enumerate(chosen_word): #looping through each character in the chosen word
            if guessed_letter == chosen_word[i]: #checking if the letter guessed by the user is equal to the current index of chosen word
                guessed_word[i] = guessed_letter #if it is equal assign the correctly guessed letter to the right position in the guessed word variable which is full of blanks
    else: 
        lives-=1 
        print(f"You have {lives} remaining" )
    print(guessed_word)
    
if guessed_word == list(chosen_word):
    print("Congrats you won")
else:
    print("You lose")


