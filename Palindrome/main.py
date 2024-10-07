#Samantha Trejo, Palindrome

word = str(input("Type in a palindrome: "))

reverse = str(word)[::-1]

if word== reverse:
    print("This is a palindrome")
else:
    print("This word isnt a palindrome")