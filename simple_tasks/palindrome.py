def is_palindrome(word):
    return word == word[::-1]

word = input("Enter a word: ")
check_word = is_palindrome(word)

if check_word:
    print(True)
else:
    print(False)