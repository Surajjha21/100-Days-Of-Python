# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo
print("\n"*3)
print("           *******-Welcome to the Silent Bidding Program-*******")
print(logo)

start=input("Do you want to start bidding?\nType of 'yes to start or 'no' for exit: ").lower()

if start=="yes":
    username=str(input("Enter your name:\n"))
    price=float(input("Enter your bid: \n$"))
    bidders = {"name":[],"price":[]}
    bidders["name"].append(username)
    bidders["price"].append(price)

    other_bid=input("Are there any other bidder?\nType of 'yes to continue or 'no' for exit: ").lower()
    print("\n"*40)
    continue_bidding=True

    while other_bid=="yes":

        continue_bidding=True
        username = str(input("Enter your name: "))
        price = float(input("Enter your bid: $"))
        bidders["name"].append(username)
        bidders["price"].append(price)
        other_bid = input("Is there any other bidder?\nType of 'yes to continue or 'no' for exit: ").lower()
        print("\n" * 40)

    if other_bid=="no":
        continue_bidding=False
        highest_bid=[0]
        for winner in bidders["price"]:
            highest_bid= max(bidders["price"])
            index_of_highest_bidder= bidders["price"].index(max(bidders["price"]))
            highest_bidder_name =  bidders["name"][index_of_highest_bidder]
        print("\n"* 40)
        print(f"The winner of this auction is {highest_bidder_name} with a bid of ${highest_bid}" )

    elif other_bid!="yes" or "no":
        print("Invalid Input")

elif start=="no":
    print("Thanks for Visit")
else:
    print ("Invalid Input")



