#import random,hangmanart,hangmanwords modules
from replit import clear
import random
from hangmanart import logo,stages
from hangmanwords import word_list

print(logo)
#pick one word randomly from the word_list by using random module
chosen_word = random.choice(word_list)


#create display list ["_","_","_","_","_"]
display=[]
length=len(chosen_word)
for i in range(length):
  display.append("_")
print(display)

previousguess=""
endgame=False
lives=6

#check all the letters in a word with guess letter by using while loop
while not endgame:

  guess=input("Guess letter ")
  clear()
  
  for position in range(length):
    if chosen_word[position]==guess:
      display[position]=guess
  
  #conver list to string
  print(" ".join(display))
  #check guess letter is present in chosen word ,if not decrease lives:count-1
  if guess not in chosen_word:
    print(f"{guess} is not in the word")
    lives-=1
    #if lives equal to zero stop the game
    if lives==0:
      endgame=True
      print("You lose")
 
   #Run the game until the blanks present in a chosen word
  if not "_" in display:
    endgame=True
    print("You win")
    #check the previous guessing letter with new guessing letter
  if  previousguess==guess:
    print(f"you already guess {previousguess} letter")
  previousguess=guess
  #print lives remaining
  print(stages[lives])
  
  


    
  
  