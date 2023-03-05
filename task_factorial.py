# ======3 task==========
# Write a function called factorial that will return the factorial of the number passed as its argument.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = 0;
print(f"Factorial of {num} is", factorial(num))