# ======1 task==========
a = 1
while a <= 100:
    a += 1
    if a % 7 == 0:
        print(a)
        
# ====2nd option=========
for x in range(101):
    if x % 7 == 0:
        print(x)

# ======2 task==========
word = input("Enter a word: ")
for y in range(len(word) - 1, -1, -1):
    print(word[y], end="")

