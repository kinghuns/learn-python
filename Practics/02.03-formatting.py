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
    change = 0.0
    print(len(stocks))
    for stock in stocks:
        total_cost += stock['shares'] * stock['price']
        total_value += stock['shares']*prices[stock['name']]
        change = stock['price'] - prices[stock['name']]
        stock['change'] =  change 
        report.append(stock)
    # report.append({'Current value': f'%0.2f'%total_value})
    # gain = total_value - total_cost
    # report.append({'Gain': f'%0.2f'%gain})
    return  report 

def make_report_data(portfolio, prices):
    '''
    Make a list of (name, shares, price, change) tuples given a portfolio list
    and prices dictionary.
    '''
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows

root = os.getcwd()
# print(root)

portfolio = read_portfolio_dict_list('Practics/Data/portfolio.csv')
print(portfolio)

prices = read_prices('Practics/Data/prices.csv')
# print(prices)

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))

report =  make_report_data(portfolio, prices)

for row in report:
    print('%10s %10d %10.2f %10.2f' % row)


print(report)
print(f'{headers[0]:^10s} {headers[1]:^10s} {headers[2]:^10s} {headers[3]:^10s}')
print(('-' * 10 + ' ') * len(headers))
for name, shares, price, change in report:
        print(f'{name:^10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
# for name, shares, price, change in report:
#         print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

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


