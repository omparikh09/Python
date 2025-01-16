import random

game_list = ["K","C"]

menu =  """
                   MENU
            Press "K" For KING
            Press "C" For Corss
        """

Round = 1
User_Won_Count = 0
User_Loss_Count = 0
status = True
while status:
    print(menu)
    print("Round :- ",Round)
    coin_drop = random.choice(game_list).upper()
    user_choice = input("Enter Your Choice :- ").upper()
    print()

    print("User Choice :- ",user_choice)
    print("Coin Drop :- ",coin_drop)
    print()

    if user_choice == "K" and coin_drop == "K":
        print("User Won The Game.")
        User_Won_Count += 1
    elif user_choice == "C" and coin_drop == "K":
        print("User Loss The Game.")
        User_Loss_Count += 1
    elif user_choice == "C" and coin_drop == "C":
        print("User Won The Game.")
        User_Won_Count += 1
    elif user_choice == "K" and coin_drop == "C":
        print("User Loss The Game.")
        User_Loss_Count += 1
    else:
        print("Invalid Input.")
    
    print("User Won Count :- ",User_Won_Count)
    print("User Loss Count :- ",User_Loss_Count)
    Round += 1

    choice = input("Do you want to continue 'y' for yes and 'n' for no :- ").upper()

    if choice == 'N' or choice == 'NO':
        break

