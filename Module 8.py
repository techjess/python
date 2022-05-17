import math
import random
def dollars_to_pesos():
    amount = float(input("How many dollars do you have? "))
    dollars  = round(amount * 20.46, 2)
    print(f"You have {dollars} in pesos")
    
def pesos_to_dollars():
    amount = float(input("How many Pesos do you have? "))
    pesos = round(amount / 20.46, 2)
    print(f"You have $ {pesos} in dollars")

def euros_to_dollars():
    amount = float(input("How many euros do you have? "))
    euros = round(amount / .95, 2)
    print(f"You have $ {euros} in dollars")

def dollars_to_euros():
    amount = float(input("How many dollars do you have? "))
    dollars = round(amount * .95, 2)
    print(f"You have $ {dollars} in dollars" )



selection = int(input("Select the Currency that you would like to conver: 1)Euros to Dollars 2) Dollars to Euros 3)Pesos to Dollars 4)Dollars to Pesos: \n"))

if selection == 1:
    euros_to_dollars()
elif selection == 2:
    dollars_to_euros()
elif selection == 3:
    pesos_to_dollars()
elif selection == 4:
    dollars_to_pesos()
else:
    print("Pickl a valid number between 1 and 4")