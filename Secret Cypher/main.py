#Samantha Trejo, Secret Cypher


def shift_cipher(text, shift):
    #initialize an empty result string
    result = ""
    
    #traverse the text
    for char in text:
        #check if character is an uppercase letter
        if char.isupper():
            #find the position in 0-25 and shift it
            new_char = chr((ord(char) + shift - 65) % 26 + 65)
            result += new_char
        #check if character is a lowercase letter
        elif char.islower():
            #find the position in 0-25 and shift it
            new_char = chr((ord(char) + shift - 97) % 26 + 97)
            result += new_char
        else:
            #if its not a letter keep it the same
            result += char
    
    return result


Message = input("Type in your message:") #asks user for the message
shift_value = 5 #shifts the legs
encoded_string = shift_cipher(Message, shift_value) #makes the message into a secret code 
print("Secret Code:", encoded_string) #print final code


