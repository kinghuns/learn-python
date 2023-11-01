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

10.20 [list comprehension](https://github.com/kinghuns/learn-python/blob/main/Notes/02_Working_with_data/06_List_comprehension.md)
The general syntax is: [ <expression> for <variable_name> in <sequence> ].
在之前列表的基础上生成一个新的列表。
- 可以增加过滤条件（类似for循环）。[ <expression> for <variable_name> in <sequence> if <condition>]
- 转换数据

### Object model: 从list到对象。
b = a, 赋值的是对象的指针，一旦a发生变化， b也会变化。
b = list(a) 则是复制列表，有两个列表对象存在。有趣的是，其元素如果有列表，则列表还是引用的状态。
**Shallow copy vs Deep copy**
```python
import copy
b = copy.deepcopy(a)
```
**Everything is an object**
```
for func, val in zip(types, row):
          converted.append(func(val))  #批量进行类型转换
```
**end of Chapter 2**
