import csv


def square(x):
    return x*x

def read_prices(filename):
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            prices[row[0]] = float(row[1])
    return prices

a = 42
b = a + 2     # Requires that `a` is defined

z = square(b) # Requires `square` and `b` to be defined

print(z)