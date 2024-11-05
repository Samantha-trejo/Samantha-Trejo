#Samantha Trejo, What is happening

class BankAccount:
    def __init__(self, account_number, balance=0): #everything starts off at 0
        self.account_number = account_number #variables set
        self.balance = balance

    def deposit(self, amount): #deposits the money from the bank
        if amount > 0:
            self.balance += amount #money will be added to balance
            return True
        return False

    def withdraw(self, amount): #withdraw money from the bank
        if 0 < amount <= self.balance:
            self.balance -= amount #money will be taken away from balance
            return True
        return False

    def get_balance(self): #the user gets the remaining balance
        return self.balance

def create_account(): #user gets to create an account
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    return BankAccount(account_number, initial_balance)

def main(): #user choices on what they would like
    accounts = {}
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ") #user will input their choice
        
        if choice == '1': #to create an account
            account = create_account()
            accounts[account.account_number] = account
            print(f"Account {account.account_number} created successfully!")
        
        elif choice in ['2', '3', '4']: 
            account_number = input("Enter account number: ")
            if account_number in accounts:
                account = accounts[account_number]
                if choice == '2': #user deposits the money
                    amount = float(input("Enter deposit amount: "))
                    if account.deposit(amount):
                        print(f"Deposited ${amount:.2f} successfully!")
                    else:
                        print("Invalid deposit amount.")
                elif choice == '3': #user withdraws the money
                    amount = float(input("Enter withdrawal amount: "))
                    if account.withdraw(amount):
                        print(f"Withdrawn ${amount:.2f} successfully!") #user has enough to withdraw
                    else:
                        print("Invalid withdrawal amount or insufficient funds.") #user wont have enough to take out
                else:
                    print(f"Current balance: ${account.get_balance():.2f}") #check the current balance
            else:
                print("Account not found.") #print if account not found
        
        elif choice == '5': #user will exit the bank and be thanked
            print("Thank you for using our banking system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.") #any other choice other than 1-5 wont work

if __name__ == "__main__":
    main()