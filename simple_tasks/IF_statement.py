# == 1 task ==

a = 100
b = 200
if (a == b):
    print("variables and b are equal")
else:
    print("variables a and b are not equal")

# == 2 task ==

print("What is your name?")
name = input()

age = int(input("What is your age?"))
timeleft = 21 - age
if age < 21:
    print(f"Entry to the club is not allowed, pls return in {timeleft} years")
else:
    print ("Welcome to the club!")