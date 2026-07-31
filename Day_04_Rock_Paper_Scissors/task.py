
import random
rock ='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper ='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors ='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options_list =[rock, paper, scissors]

select=int(input("What do you choose? \nType 0 for Rock, 1 for Paper or 2 for Scissors. \nType: "))

if select > 2 or select < 0:
    print("INVALID OUT")
else:
    print("You select")



    if select==0:
        print(rock)
    elif select==1:
        print(paper)
    elif select==2:
        print(scissors)
    print("Computer Select")
    computer_decision= random.choice(options_list)
    print(computer_decision)

    if computer_decision== rock and select==0:
            print("DRAW")
    elif computer_decision==paper and select==1:
            print("DRAW")
    elif computer_decision==scissors and select==2:
            print("DRAW")
    elif computer_decision==rock and select==2:
            print("YOU LOSE")
    elif computer_decision==scissors and select==1:
            print("YOU LOSE")
    elif computer_decision == paper and select == 0:
            print("YOU LOSE")
    else:
            print("YOU WON")




