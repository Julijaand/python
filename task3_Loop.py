# ======1 task==========
a = 1
while a <= 100:
    a += 1
    if a % 7 == 0:
        print(a)

# ======2 task==========
word = input("Enter a word: ")
for char in range(len(word) - 1, -1, -1):
    print(word[char], end="")

