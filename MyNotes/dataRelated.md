### Map reduce
[Mapreduce 基本概念](https://time.geekbang.org/column/article/423595)

python的数据处理也是遵从类似的逻辑，Sequences用于处理数据， zip则是map, 而Collection所提供的方法，如Counter、Sum等则是reduce的实现。

### 数据的重新组织
```python
names = { s['name'] for s in portfolio }
for s in portfolio:
    holdings[s['name']] += s['shares']

portfolio_prices = { name: prices[name] for name in names }
```

