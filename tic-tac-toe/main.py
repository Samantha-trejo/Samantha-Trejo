#Samantha Trejo, Tic-Tac-Toe game

def main():
    print("Welcome to Tic-Tac-Toe!")
    print("You are X and the computer is O.")
    print("Enter your move as row and column numbers (0, 1, or 2).")

    while True:
        print_board(board)  # Print the current state of the board
        
        # User move
        while True:
            try:
                row = int(input("Enter the row (0, 1, or 2): "))  # Get the row from the user
                col = int(input("Enter the column (0, 1, or 2): "))  # Get the column from the user
                # Add the rest of your code here


import random  # Import the random module for generating random moves for the computer

# Initialize the board as a 3x3 grid filled with spaces
board = [[" " for _ in range(3)] for _ in range(3)]


def print_board(board):
    # Function to print the current state of the board
    for row in board:
        print("|".join(row))  # Print the row with '|' as separators
        print("-" * 5)  # Print a horizontal line after each row


def check_winner(board):
    # Function to check if there is a winner
    # Check rows and columns for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]  # Return the winner ('X' or 'O')
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]  # Return the winner ('X' or 'O')
    
    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]  # Return the winner ('X' or 'O')
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]  # Return the winner ('X' or 'O')
    
    return None  # Return None if there is no winner


def make_move(board, row, col, player):
    # Function to make a move on the board
    if board[row][col] == " ":
        board[row][col] = player  # Place the player's mark on the board
        return True  # Return True if the move was successful
    return False  # Return False if the move was not successful


def computer_move(board):
    # Function for the computer to make a random move
    while True:
        row, col = random.randint(0, 2), random.randint(0, 2)  # Generate random row and column
        if make_move(board, row, col, "O"):
            break  # Break the loop if the move was successful
