import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
input=int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
game=[rock,paper,scissors]
if input==0:
    print(game[0])
elif input == 1:
    print(game[1])
elif input == 2:
    print(game[2])
else:
    print("Invalid choice!")
computer_input=random.randint(0,2)
if computer_input==0:
    print(game[0])
elif computer_input == 1:
    print(game[1])
elif computer_input == 2:
    print(game[2])
else:
    print("Invalid choice!")



if(input==computer_input):
    print("Tie")
elif(input==1 and computer_input==2)or(input==2 and computer_input==0) or(input==0and computer_input==1):
    print("You Lose")
else:
    print("You Win")