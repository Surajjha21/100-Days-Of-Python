print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print()
path=input('Your\'re at Two Way Road Select your path "👉Right" or "👈Left": \n').lower()
if path=="left":
    round_2=input('You\'ve come to a lake.\n There is an Island in the middle of the lake.\n Type "swim"🏊🏼 to swim across. \n           OR \nType "wait"⌛ to wait for a boat🚣: \n').lower()
    if round_2=="wait":
        door=input ('There are 3 doors on this Island. Which door do you choose? \nType "RED"🟥,"YELLOW"🟨,"BLUE"🟦: \n').lower()
        if door=="red":
            print("Burned by Fire🔥 \n 💥Game Over💥")
        elif door=="blue":
            print("Eaten by Beasts👹. \n 💥Game Over💥")
        elif door == "yellow":
            print("🏆You Win🏆")
        else:
            print("Wrong Input \n    ❌Game Over❌")
    else:
             print('You\'ve been attacked by angry CROCODILE🐊. \n           💥Game Over💥')
else:
    print('you\'ve been fell into a hole🕳️ \n        💥Game Over💥')