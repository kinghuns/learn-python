records = []  # Initial empty list

with open(r'Data\portfolio.csv', 'rt') as f:
    next(f) # Skip header
    for line in f:
        row = line.split(',')
        records.append((row[0], int(row[1]), float(row[2])))

for k in records:
    print(k[0], " :" ,k[1]*k[2])