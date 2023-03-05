# ====== 1 task ======
# Write a Python function to find the Max of three numbers.

numbers = [100, 2, 300, 10, 11, 1000]
max_number = max(numbers)
print(max_number)

# 2nd option
def max_number2(a, b, c):
    numbers = [a, b, c]
    for alfa in numbers:
        return max(numbers)

print(max_number2(10, 20, 30))

# ====== 2 task ======
# Write a Python program to reverse a string.

def reverse_string(word):
    word = [word[y] for y in range(len(word) - 1, -1, -1)]
    return "".join(word)
    print(reverse_string(word[y]), end="")
s = "1234abcd"
print(reverse_string(s))

# 2nd option
def reversed_string(text):
    reversed_text = ""
    for x in text:
        reversed_text = x + reversed_text
    return reversed_text
print (reversed_string("Hello, World!"))

# ====== 3 task ======

def sum_numbers(*digits: tuple)->float:
    """Result is sum of digits"""
    result = sum(digits)
    return result
print((sum_numbers(1, 2, 3)))
print((sum_numbers(8, 20, 2 )))
print((sum_numbers(12.5, 3.147, 98.1)))
print((sum_numbers(1.1, 2.2, 5.5)))