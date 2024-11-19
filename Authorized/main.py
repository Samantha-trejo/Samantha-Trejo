#Samantha Trejo, Authorized

#List of authorized users
authorized_users = ['alice', 'bob', 'charlie', 'dave', 'eve', 'frank', 'grace', 'heidi']
admin_users = ['alice']

#Function to check user status
def check_user_status(user):
    if user in admin_users:
        return 'Admin'
    elif user in authorized_users:
        return 'User'
    else:
        return 'Not Authorized'

#Ask for the username
username = input("Enter your username: ").lower()

#Check and print the user status
status = check_user_status(username)
print(f"{username.capitalize()} is {status}.")
