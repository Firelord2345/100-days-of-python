import random
def display_card():
    card=[2,3,4,5,6,7,8,9,10,10,10,10,11]
    choice=random.choice(card)
    return choice

def card_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    elif 11 in cards and sum(cards)>21:
          cards.remove(11)
          cards.append(1)

    return sum(cards)
def compare(u_score,c_score):
    if u_score==c_score:
          return "Draw"
    elif c_score==0:
        return "Lose,opponent won"
    elif u_score==0:
        print("Win with BlackJacK")
    elif u_score>21:
        print(" You Lose")
    elif c_score>21:
        print("Opponent Loss")
    elif u_score>c_score:
        print("You win")
    else:
        return "You Lose"
def play():
    user_card=[]
    computer_card=[]
    for i in range(2):
      user_card.append(display_card())
      computer_card.append(display_card())
      

    is_game_over=False
    while is_game_over!=True:
        user_score=card_score(user_card)
  

        computer_score=card_score(computer_card)
        print(user_card,user_score)
        print(computer_card[0])
        if user_score== 0 or computer_score==0 or user_score>21:
             is_game_over=True
        else:
            user=input("Type y to add a card and n to pass ").lower()
            if user=='y':
                 user_card.append(display_card())
                 is_game_over=False
            else:
                 is_game_over=True
    while computer_score!=0 and computer_score<17:
     computer_card.append(display_card())
     computer_score=card_score(computer_card)
    print(f"Your card {user_card},score{user_score}")
    print(f"Computer card {computer_score},score{computer_score}")
    compare(user_score,computer_score)
    replay = input("Do you want to play again? Type 'y' to play or 'n' to exit: ").lower()
    while replay=='y':
       print("\n"*20)
       play()
       
play()