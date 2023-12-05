# -----------1 option----------------

import math

number = int(input("Please insert number: "))
num_factorial = math.factorial(number)
print(f"The factorial of {number} is : ", num_factorial)

# -----------2 option----------------

number = int(input("Please insert number: "))
factorial = 1

for i in range(1, number+1):
    factorial = factorial * i

print(f"The factorial of {number} is : ", factorial)

# -----------3 option----------------

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = 0
print(f"Factorial of {num} is", factorial(num))