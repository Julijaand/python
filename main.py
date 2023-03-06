print("Welcome to the Best Bank")
Trials = 3
UserPin = 1234

while Trials != 0:
    Pin = int(input("Please enter your 4 digit Pin Number: "))
    if Pin != UserPin:
        Trials -= 1
        print("Incorrect Pin Number, You Have", Trials, "Trials left")
    else:
        UserChoice = input("d: Deposit or w: Withdraw: ")
        if UserChoice == "d":
            UserDeposit = input("Enter the amount you would like to deposit")
            print(UserDeposit, "Cash has been deposited to your account")
        if UserChoice == "w":
            UserWithdraw = input("Enter the amount you would like to withdraw")
            print(UserWithdraw, "Cash has been withdrawn from your account")
    UserExit = input("Would you like to continue? Y/N: ")
    if UserExit == "N":
        print("Thank you for using Best Bank")
        break
