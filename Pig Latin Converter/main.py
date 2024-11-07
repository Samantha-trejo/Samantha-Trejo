#Samantha Trejo, Pig Latin Converter

def convert_to_pig_latin(word):
    # Convert the word to lowercase
    word = word.lower()
    # Check if the first letter is a vowel
    if word[0] in 'aeiou':
        # If it is, add 'way' to the end of the word
        pig_latin = word + 'way'
    else:
        # If it's not, move the first letter to the end and add 'ay'
        pig_latin = word[1:] + word[0] + 'ay'
    return pig_latin

word = input("Type in any word:") #Asking user for any word
print(convert_to_pig_latin(word)) #Printing the word in piglatin