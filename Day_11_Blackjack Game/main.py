import random
print("WELCOME TO BLACKJACK")
start=input("Type 'Yes' to start or 'No' to exit: ").lower()

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
dealer_cards = []

if start=="yes":

    player_name=input("Enter Your Name:-  ").title()
    print("\n"*3)
    for shuffle_cards in range(0, 2):
        player_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))
    print(f"{player_name} Cards: {player_cards} ")
    print(f"Dealer's Cards: {dealer_cards[0]},*")

    def game():

        player_cards_sum=sum(player_cards)
        dealer_cards_sum=sum(dealer_cards)
        
        if player_cards_sum == 21:
            print("****BLACKJACK****")
            print(f"{player_name} Win")
            print()

        elif player_cards_sum<21:

            for shuffle_cards in range(0,1):
                continue_picking_cards = input("Do you want to pick new card? Type 'Yes' for pick 'No' for Standby. \n").lower()
                if continue_picking_cards == "yes":
                    player_cards.append(random.choice(cards))
                    player_cards_sum = sum(player_cards)
                    print(f"{player_name} Cards:{player_cards} and sum: {player_cards_sum}")
                    print(f"Dealer's Cards: {dealer_cards[0]},*")

                    if player_cards_sum > 21:
                        print("***BUST***")
                        print(f"{player_name} Lose")
                    else:
                        game()



                elif continue_picking_cards == "no":
                    print(dealer_cards)




    game()


elif start=="no":
    print("Thanks for visiting")

else:
    print("Invalid Input")
