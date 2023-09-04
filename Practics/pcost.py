import gzip
import os

def portfolio_cost(filename):
    f = open(filename, 'rt')
    headers = next(f).split(',')
    total_cost = 0.0
    for line in f:
        row = line.split(',')
        row[2] = row[2].strip()
        total_cost += int(row[1]) * float(row[2])
    f.close()
    return total_cost

# print('open file with gzip:\n')
# with gzip.open('Data/portfolio.csv.gz', 'rt') as f1:
#     for line in f1:
#         print(line)
# f1.close()
cost = portfolio_cost('Data/portfolio.csv')
print('Total cost:', cost)

