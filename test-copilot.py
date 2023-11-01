from queue import Queue
import random

# 创建一个队列
my_queue = Queue()

# Convert a time string such as "4:00pm" to minutes past midnight
def minutes(tm):
    am_pm = tm[-2:]
    fields = tm[:-2].split(":")
    hour = int(fields[0])
    minute = int(fields[1])
    if hour == 12:
       hour = 0
    if am_pm == 'pm':
       hour += 12
    return hour*60 + minute

# Convert time in minutes to a format string
def minutes_to_str(m):
    frac,m = math.modf(m)
    hours = m//60
    minutes = m % 60
    seconds = frac * 60
    return "%02d:%02d.%02.f" % (hours,minutes,seconds)


# Read the stock history file as a list of lists
def read_history(filename):
    result = []
    f = open(filename)
    next(f)
    for line in f:
        str_fields = line.strip().split(",")
        fields = [eval(x) for x in str_fields]
        fields[3] = minutes(fields[3])
        result.append(fields)
    return result


"""
Ask the user for their name and say "Hello"
"""
def hello():
    name = input("What is your name? ")
    print("Hello,", name)   

"""
1. Create a list of first names
2. Create a list of last names
3. Combine them randomly into a list of 100 full names
"""
def random_names():
    first_names = ["John", "Jane", "Bob", "Alice", "Mary", "Mike", "Sue"]
    last_names = ["Smith", "Jones", "Williams", "Brown", "Davis", "Miller"]
    full_names = []
    for i in range(100):
        full_names.append(random.choice(first_names) + " " + random.choice(last_names))
    return full_names

"""
Table customers, columns = [CustomerId, FirstName, LastName, Company, Address, City, State, Country, PostalCode, Phone, Fax, Email, SupportRepId]
Create a MySQL query for all customers in Texas named Jane
"""
query = "SELECT * FROM customers WHERE State = 'TX' AND FirstName = 'Jane'"

"""
read MNIST dataset
"""
import gzip
import numpy as np

def read_mnist(filename):
    with gzip.open(filename, 'rb') as f:
        data = np.frombuffer(f.read(), np.uint8, offset=16)
    return data.reshape(-1, 28, 28)

"""
Generate a function to add two numbers
"""
def add(x,y):
    return x+y





