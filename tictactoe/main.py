#Samantha Trejo, Tic-Tac-Toe

import random

print("Welcome to Tic-Tac-Toe!")
print("You are X and the computer is O.")
print("Enter your move as row and column numbers (0, 1, or 2).")


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    return None


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        if current_player == "X":
            row = int(input("Enter the row (0, 1, 2): "))
            col = int(input("Enter the column (0, 1, 2): "))
            if board[row][col] == " ":
                board[row][col] = current_player
                if check_winner(board):
                    print_board(board)
                    print("X wins!")
                    break
                current_player = "O"
        else:
            while True:
                row = random.randint(0, 2)
                col = random.randint(0, 2)
                if board[row][col] == " ":
                    board[row][col] = current_player
                    if check_winner(board):
                        print_board(board)
                        print("O wins!")
                        return
                    current_player = "X"
                    break


        if all(cell != " " for row in board for cell in row):
            print_board(board)
            print("It's a tie!")
            break


# Start the game
tic_tac_toe()
