import gzip
import os
import csv

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

def read_prices(filename):
    prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        # headers = next(rows)
        for row in rows:
            try:
                # holding = {row[0]:float(row[1])}
                # print(holding)
                prices[row[0]] = float(row[1])
            except:
                pass
        f.close
    return prices

def read_portfolio_dict_list(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        # print(headers)
        for row in rows:
            holding = {headers[0]:row[0], 
                       headers[1]:int(row[1]),
                       headers[2]:float(row[2])}
            portfolio.append(holding)
        f.close()
    return portfolio         

def make_report(stocks, prices):
    report =[]
    total_cost = 0.0
    total_value = 0.0
    print(len(stocks))
    for stock in stocks:
        total_cost += stock['shares'] * stock['price']
        total_value += stock['shares']*prices[stock['name']]
    report.append({'Current value': total_value})
    report.append({'Gain': total_value - total_cost})
    return  report 

root = os.getcwd()
# print(root)

portfolio = read_portfolio_dict_list('Practics/Data/portfolio.csv')
print(portfolio)

prices = read_prices('Practics/Data/prices.csv')
# print(prices)

report =  make_report(portfolio, prices)
print(report)

# # Calculate the total cost of the portfolio
# total_cost = 0.0
# for s in portfolio:
#     total_cost += s['shares']*s['price']

# print('Total cost', total_cost)

# # Compute the current value of the portfolio
# total_value = 0.0
# for s in portfolio:
#     total_value += s['shares']*prices[s['name']]

# print('Current value', total_value)
# print('Gain', total_value - total_cost)


