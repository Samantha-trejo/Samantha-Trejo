#Samantha Trejo, Tic-Tac-Toe game

import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    #Check rows, columns, and diagonals for a winner
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return True

    for col in range(3):
        if all(board[row][col] == board[0][col] and board[0][col] != " " for row in range(3)):
            return True

    if all(board[i][i] == board[0][0] and board[0][0] != " " for i in range(3)):
        return True

    if all(board[i][2 - i] == board[0][2] and board[0][2] != " " for i in range(3)):
        return True

    return False

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    turn = "X"
    for _ in range(9):
        print_board(board)
        if turn == "X":
            row = int(input("Enter the row (0-2) for 'X': "))
            col = int(input("Enter the column (0-2) for 'X': "))
        else:
            row, col = random.choice([(i, j) for i in range(3) for j in range(3) if board[i][j] == " "])
            print(f"Computer placed 'O' at ({row}, {col})")

        if board[row][col] == " ":
            board[row][col] = turn
            if check_winner(board):
                print_board(board)
                print(f"{turn} wins!")
                return
            turn = "O" if turn == "X" else "X"
        else:
            print("Invalid move, try again.")

    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    main()