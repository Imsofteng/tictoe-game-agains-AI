#Tic toe game for practise of python...

import random

board = [" " for _ in range(9)]

#here we will print the tic-tac-toe board 
def print_board():
    print("  1 | 2 | 3 ")
    print(" ---|---|---")
    print("  4 | 5 | 6 ")
    print(" ---|---|---")
    print("  7 | 8 | 9 ")

    for i in range(0, 9, 3):
        print(f"  {board[i]} | {board[i + 1]} | {board[i + 2]} ")

# here i used Function to check if a player has won
def check_win(player):
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# here i used Function to check if the board is full
def check_full():
    return " " not in board

# this function Function to make a player's move
def make_move(player, move):
    if board[move - 1] == " ":
        board[move - 1] = player
        return True
    else:
        print("Invalid move. The cell is already occupied.")
        return False

# this is Function for the AI to make a random move
def ai_move():
    empty_cells = [i + 1 for i, cell in enumerate(board) if cell == " "]
    if empty_cells:
        return random.choice(empty_cells)

# Main game loop
while True:
    print_board()
    player_move = int(input("Enter your move (1-9): "))
    
    if make_move("X", player_move):
        if check_win("X"):
            print_board()
            print("Congratulations! You win!")
            break
        if check_full():
            print_board()
            print("It's a draw!")
            break

        ai_player_move = ai_move()
        print(f"The AI chose cell {ai_player_move}")
        make_move("O", ai_player_move)

        if check_win("O"):
            print_board()
            print("AI wins! Better luck next time.")
            break
        if check_full():
            print_board()
            print("It's a draw!")
            break
