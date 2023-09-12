class BankAccount:
    def __init__(self,acc_no,acc_name,acc_balance):
        self.__acc_no = acc_no
        self.__acc_name = acc_name
        self.__acc_balance = acc_balance
    
    def deposit(self,amt):
        if amt > 0:
            self.__acc_balance += amt
            print(f"The sum of rupees {amt} is deposited .")
        else:
            print("Invalid amount !") 

    def withdrawl(self,amt):
        if 0<amt<=self.__acc_balance:
            self.__acc_balance -= amt
            print(f"The sum of rupees {amt} is withdrawn .")
        else:
            print("Invalid amount !")

    def display(self):
        print(f"Account number      : {self.__acc_no}")
        print(f"Account holder name : {self.__acc_name}")
        print(f"Balance             : {self.__acc_balance}")


def main():

    account = BankAccount(1234567890,'Dhanush',100000)
    choice = input("Enter your choice (deposit/withdraw/display) : ")
    if choice == 'deposit':
         amt = float(input("Enter amount to deposit : "))
         account.deposit(amt)
         account.display()
    elif choice == 'withdraw':
         amt = float(input("Enter amount to withdraw : "))
         account.withdrawl(amt)
         account.display()
    elif choice == 'display':
         account.display()
    else:
         print(f"Wrong choice : {choice} \n")
         print("\n\t\t Available Choices \t\t\n")
         print("\n\t\t _________________ \t\t\n")
         print("\n deposit \n withdraw \n display \n")
         print("\n Note : choices are case sensitive !")
main()