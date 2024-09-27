import random
EASY_GUESS=10
HARD_GUESS=5
def guess_chance(choice):
    if choice=='easy':
        return EASY_GUESS
    else:
        return HARD_GUESS

def sol(x,y,turns):
    if x>y:
             print("Its larger than the guess\n")
             turns-=1
             return turns
             
    elif x<y:
             print("Its smaller than the guess\n") 
             turns-=1
             return turns
    else:
             print("Correct  guess\n") 
             return
def guess():
    print("WELCOME TO THE NUMBER GUESSING ")
    print("Thinking of number between 1-100 ")
    z=input("Enter the mode easy or hard ").lower()
    if z=="easy":
        print(f"Guess chance {EASY_GUESS}")
    else:
        print(f"Guess chance {HARD_GUESS}")   
    chances=guess_chance(z)
    y=random.randint(1,100)
    turns=chances
    while turns!=0 :
      
       x=int(input("Enter the number"))
       turns=sol(x,y,turns)
       if x == y:
            # If correct guess, end the game
            break
        
       print(f"You have {turns} turns left.")
    if turns == 0 and x != y:
        print(f"You're out of guesses. The correct number was {y}.")
    while input("Enter to continue: y or n ")=='y':  
           guess()
    
guess()