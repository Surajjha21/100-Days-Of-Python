from art import logo

def add(n1,n2):
    return round((n1+n2),2)
def subtract(n1,n2):
    return round((n1-n2),2)
def multiply(n1,n2):
    return round((n1*n2),2)
def divide(n1,n2):
    return round((n1/n2),2)

operators={"+":add,
"-":subtract,
"*":multiply,
"/":divide}

def calculator():
    print(logo)
    game=True
    num1=float(input("Enter 1st Number: "))

    while game:
        for symbol in operators:
            print(symbol)

        choose_operator= input("Select Operator: ")

        num2=float(input("Enter 2nd Number: "))

        output=operators[choose_operator](n1=num1,n2=num2)
        print(f"{num1} {choose_operator} {num2} = {output}")

        want_to_continue=input("Do you want to continue the calculation with your previous answer? if yes press 'Y' or 'N' start from new number or 'E' for exit.  \n").lower()

        if want_to_continue=="y":
                num1=output
        elif want_to_continue=="n":
                game=False
                print("\n"*20)
                calculator()
        else:
             game=False
             print(f"Thanks for Using my CALC.")
calculator()