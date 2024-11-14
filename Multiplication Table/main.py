#Samantha Trejo, Multiplication Table

#Ask the user for a number
number = int(input("Enter a number to see its multiples: "))


#Using a for loop to print multiples of the number 
print("Multiples of", number, "from 0 to 12:")
for i in range(13):
    print(f"{number} * {i} = {number * i}")






#Printing the header row
print("   |", end="")
for i in range(13):
    print(f"{i:3}", end=" ")
print("\n" + "-" * 50)


#Using nested for loops to print the multiplication table
for i in range(13):
    print(f"{i:2} |", end="")  #Print row label
    for j in range(13):
        print(f"{i * j:3}", end=" ")
    print()
