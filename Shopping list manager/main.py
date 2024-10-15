#Samantha Trejo, Shopping list manager

print("Shopping List")

list = ["milk", "cereal", "bananas"]
print(list)
while True:
    action = input("""What would you like to do?
                   Enter 1 to add item
                   Enter 2 to remove item
                   Enter 3 to leave the list:\n""")
    

    if action =="1":
        add = input("What would you like to add?") 
        list.append(add)

    elif action =="2":
        subtract = input("What would you like to remove?")
        list.remove(subtract)

    else:
        print("Have a nice day!")
        break
    print(list)

