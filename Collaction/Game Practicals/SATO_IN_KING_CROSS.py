import random

game_list = ["K","C"]

menu =  """
                   MENU
            Press "K" For KING
            Press "C" For Corss
        """

Round = 1
Amount_Enter = 0
Amount_Exit = 0
status = True
while status:
    print(menu)
    print("Round :- ",Round)
    coin_drop = random.choice(game_list).upper()
    user_choice = input("Enter Your Choice :- ").upper()
    amt = int(input("Enter a Amount :- "))
    Amount_Enter += amt
    print()

    print("User Choice :- ",user_choice)
    print("Coin Drop :- ",coin_drop)
    print("Amount You Put :- ",amt)
    print()

    if user_choice == "K" and coin_drop == "K":
        print("User Won The Game.")
        print(f"You Won Amount :- {amt*2}")
        Amount_Exit += (amt*2)
    
    elif user_choice == "C" and coin_drop == "K":
        print("User Loss The Game.")
        print(f"You Won :- {amt*0}")

    elif user_choice == "C" and coin_drop == "C":
        print("User Won The Game.")
        print(f"You Won Amount :- {amt*2}")
        Amount_Exit += (amt*2) 
    
    else:
        print("User Loss The Game.")
        print(f"You Won :- {amt*0}")

    Round += 1

    choice = input("Do you want to continue 'y' for yes and 'n' for no :- ").upper()

    if choice == 'N' or choice == 'NO':
        break
    
print("User Enter Money :- ",Amount_Enter)
print("User Won Money :- ",Amount_Exit)

if Amount_Enter < Amount_Exit:
    print("Profit :- ",Amount_Exit-Amount_Enter)
elif Amount_Enter > Amount_Exit:
    print("Loss :- ",Amount_Enter-Amount_Exit)

