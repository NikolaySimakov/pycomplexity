# pycomplexity

## 🤔 What is this?

...

## Installation

To install using ``pip``:

```
$ pip install pycomplexity
```

## Get started

```python
from pycomplexity import BigO

big_o = BigO()

@big_o.complexity
def your_func():

    count = 0
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for el in arr:
        count += el

    return count
```

Console returns ``output``:

```
Сomplexity of algorithm: O(N)
Memory of algorithm: O(1)
```


## 📖 Documentation

Full documentation see [here](http://werlewkn.com).
