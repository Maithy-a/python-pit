
def atm():
    balance = 1000
    pin = 2600
    attempts =0

    while attempts <3:
        try:
            print("SIMP-ATM 🏧:")
            entered_pin = int(input("Enter your 4-Digit PIN🔐: "))
            if entered_pin == pin:
                print("PIN Accepted✅\n")
                break
            else:
                attempts += 1
                print(f"❌Incorrect PIN.\n{3 - attempts} Attempts Remaining.\n")
            if attempts == 3:
                print("⛔Too many tries.\nAccess Denied.\n")
                return
        except ValueError:
            print("ℹ️ Invalid Value")

    while True:
       try:
           print("MAIN MENU:")
           print("1. Current account Balance.\n"
                 "2. Deposit to account. \n"
                 "3. Withdraw from account. \n"
                 "4. Exit ATM.")
           option = int(input("Select an Option to Continue » "))

           if option == 1:
               print(f"Current Balance ≈ Kes {balance:.2f} \n")

           elif option == 2:
               deposit = float(input("Enter Deposit Amount: "))
               if deposit <= 0:
                   print("Invalid Deposit Amount.\n")
               else:
                   balance += deposit
                   print(f"Kes  {deposit} Deposited.\n"
                         f"New Balance ≈ Kes {balance:.2f}. \n")

           elif option == 3:
               withdrawal = float(input("Enter amount your wish to withdraw:"))
               if balance >= withdrawal > 0:
                   balance -= withdrawal
                   print(f"Kes {withdrawal} withdrawn✅.\n"
                         f"New Balance ≈ {balance:.2f}\n")
               elif withdrawal > balance:
                   print(f"Insufficient fund."
                         f"\nCurrent Balance ≈ Kes {balance:.2f} \n")
               else:
                   print("⛔Invalid amount.\n")

           elif option == 4:
               print("Exiting ATM, Good Bye👋")
               break

       except ValueError as e:
           print("Invalid Values.")
           print(f"Error{e}")
atm()
