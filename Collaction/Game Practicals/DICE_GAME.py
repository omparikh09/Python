import random

print("Welcome The Dice Game")

rounds = int(input("Enter a Number You Went to Play The Round :- "))

Player_score = 0
Computer_score = 0

for i in range(1, rounds + 1):
    print(f"Round {1}")

    input("Press Enter to roll the dice By Player :- ")
    Player_roll = random.randint(1, 6)
    print(f"You Rolled :- {Player_roll}")

    Computer_roll = random.randint(1, 6)
    print(f"Computer Rolled :- {Computer_roll}")

    if Player_roll > Computer_roll:
        print("Player Win The Game!")
        Player_score += 1
    elif Computer_roll > Player_roll:
        print("Computer Win The Game!")
        Computer_score += 1
    else:
        print("It's a Tie")

    print("Player Score :- ",Player_score)
    print("Computer Score :- ",Computer_score)