import random

import hangmanwords
from hangmanarts import logo,stages
lives=7
print(logo)
# Randomly choose a word from a list
chossen_word=random.choice(hangmanwords.word_list)

# print(chossen_word)
replace=[]
for j in range(len(chossen_word)):
    replace += '_'
print(replace)
incorrect_guesses = 0
# max_incorrect_guesses = len(chossen_word)
while  lives>0:
     guess=input("\nGuess the letter ").lower()

     for i in range(len(chossen_word)):
          if guess == chossen_word[i]:
              replace[i] = guess
     print(replace)
     if guess not in chossen_word:
         print(stages[incorrect_guesses])
         lives-=1
         incorrect_guesses+=1


         print(f"opps wrong guess {lives}")
     if '_' not in replace:
         print("Congratulations! You've won!")
         break

if '_' in replace:
    print(f"Sorry, you've lost. The word was '{chossen_word}'.")

print(f"The word was: {chossen_word}")
