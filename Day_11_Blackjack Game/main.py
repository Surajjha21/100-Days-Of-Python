import random
print("WELCOME TO BLACKJACK")
start=input("Type 'Yes' to start or 'No' to exit: ").lower()

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []
dealer_cards = []

if start=="yes":
    player_name=input("Enter Your Name.\n ")

    for shuffle_cards in range(0, 3):
        player_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))

        position=player_cards.index(11)
        dealer_position=dealer_cards.index(11)
        for A in player_cards:
            if A==11:
                if sum(player_cards)>21:
                    player_cards[position]=1
                else:
                    A=11

            # if sum(dealer_cards) > 21:
            #     dealer_cards[dealer_position] = 1
            # else:
            #     cards[0] = 11

    print(player_cards)
    print(dealer_cards)












elif start=="no":
    print("Thanks for visiting")

else:
    print("Invalid Input")