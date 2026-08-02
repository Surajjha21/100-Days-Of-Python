def blackjack():
    print ("\n"*3)
    import random
    print("WELCOME TO BLACKJACK")
    start=input("Type 'Yes' to start or 'No' to exit: ").lower()

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    # name_mapping= {cards[0]:"A",cards[5]:"J",cards[11]:"Q",cards[12]:"K", cards[1]:"2", cards[2]:"3", cards[3]:"4", cards[4]:"5", cards[5]:"6", cards[6]:"7", cards[7]:"8", cards[8]:"9", cards[9]:"5"}
    player_cards = []
    dealer_cards = []

    if start=="yes":
        
        player_name=input("Enter Your Name:-  ").title()
        print("\n"*3)
        
        for shuffle_cards in range(0, 2):
            
            player_cards.append(random.choice(cards))
            dealer_cards.append(random.choice(cards))
        
        while 11 in player_cards and sum(player_cards)>21:
            player_cards.remove(11)
            player_cards.append(1)

        while 11 in dealer_cards and sum(dealer_cards)>21:
            dealer_cards.remove(11)
            dealer_cards.append(1)  

        print(f"{player_name} Cards:{player_cards} and sum: {sum(player_cards)}")
        print(f"Dealer's Cards: {dealer_cards[0]},* and sum: {(dealer_cards[0])}")
        print("\n" * 3)

        def game():

            player_cards_sum=sum(player_cards)
            dealer_cards_sum=sum(dealer_cards)

            if player_cards_sum == 21:
                print("****BLACKJACK****")
                print(f"{player_name} Win")
                print("\n" * 5)
                
            elif player_cards_sum<21:

                continue_picking_cards = input("Do you want to pick new card? Type 'Yes' for pick 'No' for Standby. \n").lower()
                
                if continue_picking_cards == "yes":
                    
                    player_cards.append(random.choice(cards))
                    # player_cards_sum = sum(player_cards)
                    while 11 in player_cards and sum(player_cards)>21:
                                                        player_cards.remove(11)
                                                        player_cards.append(1)
                    player_cards_sum = sum(player_cards)                                    
                    print(f"{player_name} Cards:{player_cards} and sum: {player_cards_sum}")

                    if player_cards_sum==21:
                        print(f"Dealer's Cards: {dealer_cards},* and sum: {dealer_cards_sum}")

                    else:
                        print(f"Dealer's Cards: {dealer_cards[0]},* and sum: {(dealer_cards[0])}")    
                    print("\n" * 3)

                    if player_cards_sum > 21:
                        print("***BUST***")
                        print(f"{player_name} Cards:{player_cards} and sum: {player_cards_sum}")
                        print(f"Dealer's Cards: {dealer_cards} and sum: {dealer_cards_sum}")
                        print("\n" * 3)
                        print(f"{player_name} Lose")
                        print("\n" * 5)
                    else:
                        game()



                elif continue_picking_cards == "no":
                    dealer_cards_sum=sum(dealer_cards)
                    # print(player_cards)
                    # print(dealer_cards)

                    if 21>dealer_cards_sum>player_cards_sum and dealer_cards_sum>=17:
                        print(f"{player_name} Cards:{player_cards} and sum: {player_cards_sum}")
                        print(f"Dealer's Cards: {dealer_cards} and sum: {dealer_cards_sum}")
                        print(f"{player_name} Lose")
                        print("\n" * 5)

                    elif dealer_cards_sum==player_cards_sum and dealer_cards_sum>=17:
                        print(f"{player_name} Cards:{player_cards} and sum: {player_cards_sum}")
                        print(f"Dealer's Cards: {dealer_cards} and sum: {dealer_cards_sum}")
                        print("Game Draw")
                        print("\n" * 5)
                        

                    elif dealer_cards_sum==21:
                        print(f"{player_name} Cards:{player_cards} and sum: {player_cards_sum}")
                        print(f"Dealer's Cards: {dealer_cards} and sum: {dealer_cards_sum}")
                        print(f"{player_name} Lose")
                        print("\n" * 5)

                    elif 21>player_cards_sum>dealer_cards_sum and dealer_cards_sum>=17:
                        print(f"{player_name} Cards:{player_cards} and sum: {player_cards_sum}")
                        print(f"Dealer's Cards: {dealer_cards} and sum: {dealer_cards_sum}")
                        print("\n" * 2)
                        print(f"{player_name} Win")
                        print("\n" * 5)

                    while dealer_cards_sum<17:
                        dealer_cards.append(random.choice(cards))
                        

                        if 11 in dealer_cards and sum(dealer_cards)>21:
                                dealer_cards.remove(11)
                                dealer_cards.append(1)

                        
                                    
                        dealer_cards_sum=sum(dealer_cards)
                        print(f"{player_name} Cards:{player_cards} and sum: {player_cards_sum}")
                        print(f"Dealer's Cards: {dealer_cards} and sum: {dealer_cards_sum}")
                        print("\n" * 3)

                        if dealer_cards_sum>21:
                            print(f"BUST {player_name} Win")
                            print("\n" * 5)

                        elif 17<=dealer_cards_sum>player_cards_sum or dealer_cards_sum==21:
                            print(f"{player_name} Lose")
                            print("\n" * 5)

                        elif dealer_cards_sum==player_cards_sum and dealer_cards_sum>=17:
                            print("Game Draw")
                            print("\n" * 5)

                        elif 21>player_cards_sum>dealer_cards_sum and dealer_cards_sum>=17:
                                        print(f"{player_name} Cards:{player_cards} and sum: {player_cards_sum}")
                                        print(f"Dealer's Cards: {dealer_cards} and sum: {dealer_cards_sum}")
                                        print("\n" * 2)
                                        print(f"{player_name} Win")
                                        print("\n" * 5)
                        
                        
                else:
                    print("Invalid Input")

               

        game()

    

    elif start=="no":
        print("Thanks for visiting")

    else:
        print("Invalid Input")


blackjack()

restart=input("Do you want to restart the game? Type 'Yes' for restart 'No' for exit. \n").lower()
            
if restart=="yes":
    blackjack()
else:
    print("Thanks for visiting")