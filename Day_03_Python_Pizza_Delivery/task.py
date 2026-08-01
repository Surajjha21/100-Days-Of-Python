print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni_S_pizza=2
pepperoni_M_L_pizza=3
extra_cheese_price=1
bill=0
if size == "L":
    bill=25
    pepperoni = input("Do you want pepperoni on your pizza? Yes(Y) or No(N): ")
    extra_cheese = input("Do you want extra cheese? Yes(Y) or No(N): ")
elif size == "M":
         bill=20
         pepperoni = input("Do you want pepperoni on your pizza? Yes(Y) or No(N): ")
         extra_cheese = input("Do you want extra cheese? Yes(Y) or No(N): ")
elif size=="S":
        bill=15
        pepperoni = input("Do you want pepperoni on your pizza? Yes(Y) or No(N): ")
        extra_cheese = input("Do you want extra cheese? Yes(Y) or No(N): ")

else:
    print("INVALID INPUT")


if pepperoni=="Y":
    if size=="S":
        bill=bill+pepperoni_S_pizza
    else:
        bill= bill+pepperoni_M_L_pizza
if extra_cheese=="Y":
    bill=bill+extra_cheese_price
print(f"Your final bill is: ${bill}.")
