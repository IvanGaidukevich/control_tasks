import names
from random import randint

# Project 1_1B
while True:
    full_name = input("Enter your name and surname:").title().split()
    try:  # перехватываю exception, если пользователь ввел  менее или более двух слов.
        login = full_name[0][:4] + full_name[1][:1]
        print(f"{full_name[0]} {full_name[1]}: {login}")
        break
    except IndexError:
        print("You are wrong! Please try to enter the NAME and the SURNAME again")

# Project 1_2B
products_names = ["milk", "cheese", "bread", "eggs", "butter", "sweets", "cookies", "water", "tea", "coffee"]
products_prices = [82.10, 159.99, 22.50, 81.35, 150.20, 200.99, 100.50, 30.45, 56.35, 299.99]
employees_ids = [111, 112, 123, 134, 156, 157, 158, 180, 182, 183]
orders = list(zip(products_names, products_prices, employees_ids))  # получился единый список с кортежами
print(orders)

# Project 1_3B
# task 1
threshold = int(input("Enter threshold:"))
numbers = [randint(1, 100) for number in range(10)]
leveler = []
for number in numbers:
    if number > threshold:
        leveler.append("High")
    elif number < threshold:
        leveler.append("Low")
    else:
        leveler.append("Equal")  # может быть ситуация, когда число равно пороговому значению
print(f"{numbers}\n{leveler}")

# task 2
names_list = [names.get_first_name() for name in range(100)]
names_between_am = [name for name in names_list if 64 < ord(name[:1]) < 78]
other_names = [name for name in names_list if ord(name[:1]) > 77]
print(f"List of names from A to M:\n{sorted(names_between_am)}\nList of other names:\n{sorted(other_names)}")

# task 3
poem = []
acronim = " "
while acronim != "":
    acronim = input("Enter any word or press Enter for the exit:")
    poem.append(acronim)
for word in poem:
    acronim = f"{acronim}{word[:1]}"
print(acronim)
