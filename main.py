import names
import doctest
import logging
import pandas as pd
from statistics import mean, StatisticsError
from random import randint
from datetime import datetime


# Project 1_6B

def csv_data_join(filename_list: list):
    """
    Function joins data from any numbers of CSV files.
    Pandas is used. Logging is used (log.log)
    Args:
        filename_list: (list) not empty list with names of CSV files
    Exception:
        ValueError: if the list of filenames is empty,
        returns (str) 'The empty list of filenames'
        FileNotFoundError: if file or files are not found,
        returns (str) 'No such file(s)'
    Returns:
        str: (str) created file's name using scheme Y-m-d_H-M-S_updated.csv

    >>> csv_data_join([])
    'The empty list of filenames'
    >>> csv_data_join(["csv.csv"])
    'No such file(s)'
    """
    export_filename = datetime.today().strftime("%Y-%m-%d_%H-%M-%S") + "_updated.csv"
    logging.basicConfig(filename="log.log", level=logging.DEBUG, format='%(asctime)s%(levelname)s: %(message)s')
    try:
        export_df = pd.concat([pd.read_csv(filename) for filename in filename_list], ignore_index=True)
        export_df.to_csv(export_filename, index=False)
        logging.info(f"Data from other files successfully copied to {export_filename}")
        return export_filename
    except ValueError:
        logging.error("The empty list of filenames")
        return "The empty list of filenames"
    except FileNotFoundError:
        logging.error("No such file(s)")
        return "No such file(s)"
    except Exception as ex:
        logging.error(ex)
        return ex


csv_data_join(['students.csv', 'new_students.csv'])


# Project 1_5B
# task 1
def show_average_t(from_hour: int, to_hour: int, t_mesuares):
    """
    show_average_t() returns average temperature for the time period
    (from a specific hour to a specific hour in one day).
    To show average temperature from 00.00 to 00.00 next day -> enter from_hour: 0 , to_hour: 24 .

    Args:
        from_hour: (int) from which hour? numbers from 0 to 23
        to_hour: (int) to which hour? numbers from 1 to 24
        t_mesuares: (list) list of any numbers
    Exception:
        StatisticsError: if the time period has only one value == None,
        returns (str) 'Thermometer didn't work this period'
    Returns:
        float: (float) average value of temperature or (str)'Wrong time period' if from_hour >= to_hour

    >>> show_average_t(0, 24, [-5, -6, None, -6, None, -4, None, -3, -1, 0, 2, 3, 4, 5, 5, 5, 4, 4, 5, 3, 2, 2, 1, 3])
    1.1
    >>> show_average_t(2, 2, [-6, -6, None, -6, -2, -4, -3, -3, -1, 0, 2, 3, 4, 5, 5, 5, 4, 4, 5, 5, 2, 2, 1, 1])
    'Wrong time period'
    >>> show_average_t(0, 2, [None, None, 1, 1, 1, -1, -1, -3, -1, 0, 2, 3, 4, 5, 5, 5, 4, 4, 5, 3, 2, 2, 1, 3])
    'Thermometer did not work this period'
    """
    try:
        if from_hour < to_hour:
            return round(mean([measure for measure in t_mesuares[from_hour:to_hour] if measure is not None]), 2)
        else:
            return "Wrong time period"
    except StatisticsError:
        return "Thermometer did not work this period"


day_t_mesuares = [-5, -6, None, -6, None, -4, None, -3, -1, 0, 2, 3, 4, 5, 5, 5, 4, 4, 5, 3, 2, 2, 1, 3]
print(show_average_t(0, 24, day_t_mesuares))


# task 2
def tuple_maker(*nums):
    """
    tuple_maker() returns tuple with two lists: desc sorted list of negative numbers,
    and asc sorted list with positive numbers

    Args:
        nums: (*args) positive or negative numbers of any type.
    Returns:
        tuple: tuple of two lists

    >>> tuple_maker(1, 99.8, 3, 41, 5, -1, -45, 0)
    ([-1, -45], [0, 1, 3, 5, 41, 99.8])
    >>> tuple_maker(-0.999999999999999, -1000000000000000000000000)
    ([-0.999999999999999, -1000000000000000000000000], [])
    >>> tuple_maker()
    ([], [])
    """

    positive, negative = [], []
    for num in nums:
        if num >= 0:
            positive.append(num)
        else:
            negative.append(num)
    return sorted(negative, reverse=True), sorted(positive)


print(tuple_maker(-1, 0, -50, -7, 8, 11, 1001))


# task 3
def int_pow(x, n: int) -> float:
    """
    int_pow() returns the result of raising a number to an integer power

    Args:
        x: any number
        n: (int) for power of number
    Returns:
        y: (float) the result of raising a number to a power


    >>> int_pow(2.1, 4)
    19.448100000000004
    >>> int_pow(-2, 4)
    16.0
    >>> int_pow(0, 0)
    1.0
    >>> int_pow(5, 1)
    5.0
    >>> int_pow(2, -2)
    0.25

    """
    y = 1.0
    if n > 0:
        y = 1.0
        for i in range(0, n):
            y *= x
        return y
    elif n < 0:
        y = 1.0
        for i in range(0, abs(n)):
            y *= x
        y = 1 / y
        return y
    return y


def recursion_int_pow(x, n: int) -> float:
    """
    recursion_int_pow() returns the result of raising a number to an integer power (using recursion)

    Args:
        x: any number
        n: (int) for power of number
    Returns:
        y: (float) the result of raising a number to a power

    >>> recursion_int_pow(2.1, 4)
    19.448100000000004
    >>> recursion_int_pow(-2, 4)
    16.0
    >>> recursion_int_pow(0, 0)
    1.0
    >>> recursion_int_pow(5, 1)
    5.0
    >>> recursion_int_pow(2, -2)
    0.25
    """
    if n > 0:
        return float(x * recursion_int_pow(x, n - 1))
    elif n < 0:
        return 1 / float(x * recursion_int_pow(x, abs(n) - 1))
    return 1.0


print(f"{int_pow(0, 0):.2f}")
print(f"{recursion_int_pow(5, 0):.2f}")
doctest.testmod()

# Project 1_4B
data_frame = pd.read_csv("orderdata_sample.csv")
data_frame["Total"] = data_frame.Quantity * data_frame.Price + data_frame.Freight
print(data_frame[["Quantity", "Price", "Freight", "Total"]])

# Project 1_1B
while True:
    full_name = input("Enter your name and surname:").title().split()
    try:
        login = full_name[0][:4] + full_name[1][:1]
        print(f"{full_name[0]} {full_name[1]}: {login}")
        break
    except IndexError:
        print("You are wrong! Please try to enter the NAME and the SURNAME again")

# Project 1_2B
products_names = ["milk", "cheese", "bread", "eggs", "butter", "sweets", "cookies", "water", "tea", "coffee"]
products_prices = [82.10, 159.99, 22.50, 81.35, 150.20, 200.99, 100.50, 30.45, 56.35, 299.99]
employees_ids = [111, 112, 123, 134, 156, 157, 158, 180, 182, 183]
orders = list(zip(products_names, products_prices, employees_ids))
print(orders)

# Project 1_3B
# task 1
threshold = int(input("Enter threshold:"))
numbers = [randint(1, 100) for number in range(10)]
leveler = ["High" if number > threshold else "Low" if number < threshold else "Equals" for number in numbers]
print(f"{numbers}\n{leveler}")

# task 2
names_list = [names.get_first_name() for name in range(100)]
names_between_am = [name for name in names_list if "A" <= name[:1] <= "M"]
other_names = [name for name in names_list if name[:1] > "M"]
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
