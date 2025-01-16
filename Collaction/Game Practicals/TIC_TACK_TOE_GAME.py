board = [" " for i in range(9)]

print("Welcome To Tic Tack Toe Game!")
print("Board Positions :- ")
Bord_Positions = """
Menu
(" 1 | 2 | 3 ")
("---+---+---")
(" 4 | 5 | 6 ")
("---+---+---")
(" 7 | 8 | 9 ")
"""

User_1_Symbol = input("Choose Your Symbol (X OR O) :- ").upper()
while User_1_Symbol not in ["X", "O"]:
    User_1_Symbol = input("Invalid Choice. Please Choos X or O :- ").upper()

User_2_Symbol = "O" if User_1_Symbol == "X" else "X"
print(f"Player 1 is {User_1_Symbol} and Player 2 is {User_2_Symbol}")

game_over = False
current_player = "Player 1"
current_symbol = User_1_Symbol

while not game_over:
    print(Bord_Positions)
    print("Current Board :- ")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")

    position = int(input(f"Player {current_player} ({current_symbol}), Enter Your Position (1-9) :- ")) - 1

    if position < 0 or position >= 9 or board[position] != " ":
        print("Invalid move. Try again.")
        continue

    board[position] = current_symbol

    win_conditions = [
                      (0, 1, 2), (3, 4, 5), (6, 7, 8), # Horizontal
                      (0, 3, 6), (1, 4, 7), (2, 5, 8), # Vertical
                      (0, 4, 8), (2, 4, 6)            # Diagonal
                     ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == current_symbol:
            print("\nFinal board :- ")
            print(f" {board[0]} | {board[1]} | {board[2]}")
            print("---+---+---")
            print(f" {board[3]} | {board[4]} | {board[5]}")
            print("---+---+---")
            print(f" {board[6]} | {board[7]} | {board[8]}")
            print(f"{current_player} ({current_symbol}) wins!")
            game_over = True
            break
    
    if " " not in board and not game_over:
        print("\nFinal board:")
        print(f" {board[0]} | {board[1]} | {board[2]}")
        print("---+---+---")
        print(f" {board[3]} | {board[4]} | {board[5]}")
        print("---+---+---")
        print(f" {board[6]} | {board[7]} | {board[8]}")
        print("It's a draw!")
        game_over = True

    if not game_over:
        current_player = "Player 2" if current_player == "Player 1" else "Player 1"
        current_symbol = User_2_Symbol if current_symbol == User_1_Symbol else User_1_Symbol

