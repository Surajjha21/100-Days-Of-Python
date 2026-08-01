import random
import my_first_module
print("Welcome to Coin flip program")

click_to_flip = int(input("Press 1 to flip coin or any number to exit the game: "))

if click_to_flip==1:
    print(r'''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠠⠤⠤⠤⠶⠶⠤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠠⢊⣡⣶⣿⡷⠀⠀⠀⣀⣠⣤⣤⣤⣄⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢿⠿⠟⠋⠀⠀⠀⣾⠉⠀⠀⠀⣀⣤⠞⢴⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠒⠚⠛⠉⠁⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣷⣶⣶⡄⠀⢸⣿⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣉⠉⠉⠀⠀⠀⠻⣿⣿⣷⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠿⠿⢿⠆⢶⣦⣄⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣶⣶⣦⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣬⣉⣉⣛⠀⢸⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠿⠟⠁⢸⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠶⠾⠿⠿⢿⣿⣿⣿⣿⣿⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠁⠀''')

    #Outcome
    flip_coin= int(random.randint(1,2))
    decision = input('Type: "Heads" or "Tails": \n').lower()
    if flip_coin==1:
        print( r''' ╭───────╮
 │ HEAD  │
 ╰───────╯''')

    elif flip_coin==2:
        print(''' ╭───────╮
 │ TAIL  │
 ╰───────╯''')

    if flip_coin==2 and decision=="Tails".lower():
        print("You Win")
    elif flip_coin == 1 and decision == "Heads".lower():
        print("You Win")
    else:
        print("You Lose")
else:
    print("See You Again")