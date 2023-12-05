def add(x, y):
    result = x + y
    print("x + y equal to ", result)

def subtract(x, y):
    result = x - y
    print("x - y equal to ", result)

def multiply(x, y):
    result = x * y
    print("x * y equal to ", result)

def divide(x, y):
    result = x / y
    print("x / y equal to ", result)

while True:
    x = input("Please enter X ")
    if x == '':
        print("You must enter a value")
    else:
        x = int(x)
        break

while True:
    y = input("Please enter Y ")
    if y == '':
        print("You must enter a value")
    else:
        y = int(y)
        break

add(x, y)
subtract(x, y)
multiply(x, y)
divide(x, y)