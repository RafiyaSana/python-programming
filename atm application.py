# ATM APPLICATION
while True:
    account=100000
    pwd=1234
    card=input("insert the card:")
    if card=="c":
        print("welcome sana")
        password=int(input("enter the password:"))
        if password==pwd:
            option=int(input('''choose the option
                                                 1.balance
                                                 2.withdraw'''))
            if option==1:
                print("your acc bal is:",account)
            elif option==2:
                money=int(input("enter the money:"))
                print(money)
                balance=account-money
                print("rem acc bal is",balance)
            else:
                print("Invalid option")
        else:
            print("Invalid password")
    else:
        print("Invalid card")
