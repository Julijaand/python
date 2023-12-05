cars = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "owner": "Bill Johns",
    "contacts": 80002659
}

def search_dictionary(cars, key):
    if key in cars:
        return cars[key]
    else: 
        return "Key not found"

search_key = input("Enter a key: ")
value = search_dictionary(cars, search_key)
print(value)