#Samantha Trejo, Counting characters

def count_letters(grid):
    letter_counts = {}
    
    for row in grid:
        for letter in row:
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
    
    for letter, count in letter_counts.items():
        print(f"{letter}: {count}")

grid = [
    ['A', 'B', 'C', 'A', 'D'],
    ['C', 'A', 'B', 'D', 'E'],
    ['A', 'D', 'C', 'E', 'A'],
    ['B', 'A', 'C', 'A', 'D'],
    ['D', 'C', 'B', 'E', 'A']
]

count_letters(grid)