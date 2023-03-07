import interface as inte
import operations as ops

print("Welcome to the Best Bank")
Trials = 3
UserPin = 1234
user_balance = 10000
user_name = "Ms. Julija"

while Trials != 0:
    Pin = int(input("Please enter your 4 digit Pin Number: "))
    if Pin != UserPin:
        Trials -= 1
        print("Incorrect Pin Number, You Have", Trials, "Trials left")
    else:
        print("Account auhtorized!\n\n")

        def main():
            lang = int(input("\n0 - English\n1 - Latvian\n2 - Lithuanian\nSelect a language:\n"))
            print(f"You selected the {inte.get_lang(lang)} lanugage")

            UserChoice = int(input("Please select operation:\n 1  - Check balance\n 2 - Deposit money\n 3 - Withdraw money\n 4 - Exit\n"))

            if UserChoice ==  "1":
                print(f"You have {ops.get_balance()} on your account")


            if UserChoice == "2":
                UserDeposit = float(input("Enter the amount you would like to deposit"))
                print({ops.deposit(UserDeposit)}, "Cash has been deposited to your account")


            if UserChoice == "3":
                while(True):
                    UserWithdraw = float(input("Enter the amount you wish to withdraw > "))

                    if (UserWithdraw > user_balance):
                        print("Can't withdraw", UserWithdraw)
                        print("Please enter a lower amount!")
                        continue

                    else:
                        print("Withdrawing", UserWithdraw)
                        confirm = input("Confirm? Y/N > ")
                        if confirm in ('Y', 'y'):
                            user_balance -= UserWithdraw
                            print("Amount withdrawn - Rs.", UserWithdraw)
                            print("Remaining balance - Rs.", user_balance, end = "\n\n\n")
                            break

                        else:
                            print("Cancelling transaction...")
                            print("Transaction Cancelled!\n\n")
                            break

                    break

            if UserChoice == "4":
                UserExit = input("Would you like to continue? Y/N: ")
                if UserExit == "N":
                    print("Thank you for using Best Bank")
            break