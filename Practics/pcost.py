import gzip
import os
import csv

# def portfolio_cost(filename):
#     f = open(filename, 'rt')
#     headers = next(f).split(',')
#     total_cost = 0.0
#     for line in f:
#         row = line.split(',')
#         row[2] = row[2].strip()
#         total_cost += int(row[1]) * float(row[2])
#     f.close()
#     return total_cost

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
        f.close()
    return portfolio

def read_portfolio_dict_list(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        print(headers)
        for row in rows:
            holding = {headers[0]:row[0], 
                       headers[1]:int(row[1]),
                       headers[2]:float(row[2])}
            portfolio.append(holding)
        f.close()
    return portfolio         

def read_prices(filename):
    prices = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        # headers = next(rows)
        for row in rows:
            try:
                holding = {row[0]:float(row[1])}
                # print(holding)
                prices.append(holding)
            except:
                pass
        f.close
    return prices


# print('open file with gzip:\n')
# with gzip.open('Data/portfolio.csv.gz', 'rt') as f1:
#     for line in f1:
#         print(line)
# f1.close()
# cost = portfolio_cost('Data/portfolio.csv')
# print('Total cost:', cost)
root = os.getcwd()
print(root)

portfolio = read_portfolio_dict_list('Practics/Data/portfolio.csv')
print(portfolio)

# # total = 0.0
# # for name, shares, price in portfolio:
# #             total += shares*price

# # print(total)
# print(portfolio)
# prices = read_prices('G:/dev/python/learn-python-l01/Practics/Data/prices.csv')

prices = read_prices('Practics/Data/prices.csv')
print(prices)




