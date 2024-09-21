class ATM:
    
    def __init__(self):
        self.name = ""
        self.password = ""
        self.balance = 0
        print("Welcome to our Mariyama ATM...!")

    def AccountCreate(self):
        self.name = input("Enter Your name : ")
        self.password = input("Set Your new Passsword : ")
        pass2 = input("ReEnter your  password : ")

        if self.password == pass2:
            print("Account created successfully 🤩")
        else:
            print('There some issue may you try again..')
            self.AccountCreate()

    def ResetPassword(self):
        userName = input("Enter the userName : ")
        if userName == self.name:
            newPass = input("Enter your New Password :") 
            self.password = newPass

    def AmountCredit(self):
        cName = input("Enter Your name : ")
        if cName == self.name:
            Amount = int(input(f"Enter the amount you want to credit {self.name} :"))
            self.balance += Amount
            print(f"{Amount} Amount Credited to {self.name} ")
        else:
            print("User name incorrect")



bank = ATM()
# bank.AccountCreate()
# bank.ResetPassword()

while True:
    print("1. Account Create")
    print("2. Reset Password")
    print("3. Amount Credit")
    print("4. Amount Debit")
    print("5. Check balance")
    print("6. Exit")
    choice = int(input("Enter your Choice :"))
    
    if choice==1:
        bank.AccountCreate()

    elif choice == 2 :
        bank.ResetPassword()
    
    elif choice == 3:
        bank.AmountCredit()

    # elif choice == 4:
    #     bank.AmountDebeit()
    
    # elif choice == 5:
    #     bank.CheckBalance()

    elif choice == 6:
        quit()
    
    else:
        quit()




