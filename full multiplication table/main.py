#Samantha Trejo, Full Multiplication table

# Function to print the multiplication table
def print_multiplication_table():
    # Print the header row
    print("   ", end="")
    for i in range(1, 13):
        print(f"{i:4}", end="")
    print()


    # Print the table rows
    for i in range(1, 13):
        # Print the row header
        print(f"{i:2} ", end="")
        for j in range(1, 13):
            print(f"{i * j:4}", end="")
        print()


# Call the function to print the table
print_multiplication_table()
