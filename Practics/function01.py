def sumcount(n):
    '''
    Returns the sum of the first n integers
    '''
    total = 0
    while n > 0:
        total += n
        n -= 1
    return total

def greeting(name):
    print('Hello ' , name)

import math
x = math.sqrt(10)
print(x)

# file = open('Data/portfolio.csv', 'rt')
# for line in file:
#     # print(line)
#     fields = line.split(',')
#     print(fields)
#     try:
#         shares = int(fields[1])
#     except ValueError:
#         print("Couldn't parse", line)

# import urllib.request
# u = urllib.request.urlopen('http://www.python.org/')
# data = u.read()
# print(data)
# raise RuntimeError('What a kerfuffle')

greeting('World')
greeting('Brian')
