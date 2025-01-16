import random

game_list = ["R","P","S"]

menu =  """
                   Menu

            Press "R" for ROCK
            Press "P" for PAPER
            Press "S" for SCISSOR
        """

status = True
Round = 1
Computer_Won_Count = 0
User_Won_Count = 0
Tie_User_and_Computer_Count = 0
while status:
    print(menu)
    print("Round :- ",Round)
    computer = random.choice(game_list).upper()
    user_choice = input("Enter your choice :- ").upper()
    print()

    print("COMPUTER CHOICE :- ",computer)
    print("USER CHOICE :- ",user_choice)
    print()

    if user_choice == "R" and computer == "P":
        print("Computer Won The Match.")
        Computer_Won_Count += 1
    elif user_choice == "R" and computer == "S":
        print("User Won The Match.")
        User_Won_Count += 1

    elif user_choice == "P" and computer == "S":
        print("Computer Won The Match.")
        Computer_Won_Count += 1
    elif user_choice == "P" and computer == "R":
        print("User Won The Match.")
        User_Won_Count += 1

    elif user_choice == "S" and computer == "R":
        print("Computer Won The Match.")
        Computer_Won_Count += 1
    elif user_choice == "S" and computer == "P":
        print("User Won The Match.")
        User_Won_Count += 1
    
    else:
        print("--- TIE ---")
        Tie_User_and_Computer_Count += 1
    print()

    print("Computer Won Count :- ",Computer_Won_Count)
    print("User Won Count :- ",User_Won_Count)
    print("Tie Between Computer & User Count :- ",Tie_User_and_Computer_Count)

    Round += 1
    choice = input("Do You Want to Continue Press 'Y' for Yes and Press 'N' for no :- ").upper()

    if choice == 'N' or choice == 'NO':
        status = False
