

class atmUser:
    def __init__(self, acct_num, pin, balance):
        self.acct_num = int(acct_num)
        self.pin = int(pin)
        self.balance = float(balance)
        self.transaction_history = []

 # get methods
    def get_acct_num(self):
        return self.acct_num
    def get_pin(self):
        return self.pin
    def get_balance(self):
         return self.balance 
    def add_transaction(self, transaction_type, amount): 
        self.transaction_history.append((transaction_type, amount))
       
        
class atm: 

    def deposit(self, atmUser):
        deposit_amt = float(input("How much are you depositing today? ")) 
        if deposit_amt <= 0: 
            print("Invalid. Please try again.")
            return
        atmUser.balance += deposit_amt
        atmUser.add_transaction("Deposit", deposit_amt)
        print(f"You have successfully deposited ${deposit_amt}. Your new balance is ${atmUser.balance}")
        

    def withdraw(self, atmUser): 
        withdraw_amt = float(input("How much are you withdrawing today? ")) 
        if withdraw_amt <= 0:
           print("Invalid amount. Please try again.") 
           return

        if withdraw_amt > atmUser.balance:
            print("Can not complete transaction. Insufficient Funds. Please try again.")
        else: 
            atmUser.balance -= withdraw_amt
            atmUser.add_transaction("Withdraw", withdraw_amt)
            print(f"Your withdrawal of ${withdraw_amt} is complete. Your new balance is ${atmUser.balance}")

    def get_balance(self, atmUser): 
        print(f"Your balance is ${atmUser.balance}")
    
    def get_transaction_history(self, atmUser):
        print(atmUser.transaction_history)


#ATM Machine
atm_machine = atm()

# ATM Users - Hardcode
user1 = atmUser(1, 6745, 245.55)
user2 = atmUser(2, 9452, 1950.52)
user3 = atmUser(3, 2541, 6754.86)
user4 = atmUser(4, 4574, 1548.36)

# Pin lookup
user_pin_dict = {
    user1.get_pin() : user1,
    user2.get_pin() : user2,
    user3.get_pin() : user3, 
    user4.get_pin() : user4
}



# ATM Authentication

pin_prompt = int(input("Welcome to ABC Bank! Please enter your 4-digit PIN: "))

if pin_prompt in user_pin_dict:
    current_user = user_pin_dict[pin_prompt] # Sets current user based on PIN

    while True:
        option = int(input("""
            What type of transaction would you like to do today? 
                        
            1. Deposit 
            2. Withdrawal 
            3. Balance Inquiry 
            4. Transaction History
            5. Exit
            Enter here:  
            """))

        if option == 1: 
            atm_machine.deposit(current_user)
        elif option == 2: 
            atm_machine.withdraw(current_user)
        elif option == 3: 
            atm_machine.get_balance(current_user)
        elif option == 4: 
            atm_machine.get_transaction_history(current_user)
        elif option == 5: 
            print("Thank you for your transaction today!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 5 to do your transaction.")
        
           
else: 
    print("Wrong PIN. Please try again.")
       
        
    
    
