#Samantha Trejo, What are these numbers?

#Get the number from the user
number = float(input("Enter a number: "))

#Format as an integer with commas
formatted_integer = "{:,}".format(int(number))

#Format as a float with 4 decimal places
formatted_float = "{:.4f}".format(number)

#Format as a percentage
formatted_percentage = "{:.2%}".format(number / 100)

#Format as a dollar amount
formatted_dollar = "${:,.2f}".format(number)

#Print the results
print("Formatted as an integer with commas:", formatted_integer)
print("Formatted as a float with 4 decimal places:", formatted_float)
print("Formatted as a percentage:", formatted_percentage)
print("Formatted as a dollar amount:", formatted_dollar)