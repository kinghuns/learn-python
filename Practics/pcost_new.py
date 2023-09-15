import csv

import colorama
from colorama import Fore, Style

def portfolio_cost(filename):
    '''
    Computes the total cost (shares*price) of a portfolio file
    '''
    total_cost = 0.0

    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            print(rowno, record)
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            # This catches errors in int() and float() conversions above
            except ValueError:
                print( Fore.RED + f'Row {rowno}: Bad row: {row}')
                print(Style.RESET_ALL)

    return total_cost


# import sys
# if len(sys.argv) == 2:
#     filename = sys.argv[1]
# else:
#     filename = input('Enter a filename:')

# cost = portfolio_cost('Practics/Data/missing.csv')
cost = portfolio_cost('Practics/Data/portfoliodate.csv')
print('Total cost:', cost)