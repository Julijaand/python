import random

def guess_number():
    generated_number = random.randint(1, 100)

    for num_guesses in range(1, 101):
        guess_number = int(input("Guess the number between 1 and 100: "))

        if guess_number == generated_number:
            print("Congradulations, you guessed the number!")
            break
        elif guess_number > generated_number:
                print("Your number is higher than generated")
        else: 
                print("Your number is lower than generated")

    print("Number of gusses:", num_guesses)

guess_number()