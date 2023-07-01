# pycomplexity

[![PyPI version](https://img.shields.io/pypi/v/pycomplexity)](https://pypi.org/project/pycomplexity/)
[![License](https://img.shields.io/github/license/NikolaySimakov/pycomplexity)](https://github.com/NikolaySimakov/pycomplexity/blob/main/LICENSE)
[![Coverage Status](https://coveralls.io/repos/github/NikolaySimakov/pycomplexity/badge.svg?branch=master)](https://coveralls.io/github/NikolaySimakov/pycomplexity?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Python library to measure the complexity of your algorithms using the following asymptotic notations:

- [Big O](https://en.wikipedia.org/wiki/Big_O_notation)
- [Big Ω (omega)](https://en.wikipedia.org/wiki/Big_O_notation#Big_Omega_notation)
- [Big Θ (theta)](https://en.wikipedia.org/?title=Big_Theta_notation&redirect=no)

## Installation

To install using ``pip``:

```
$ pip install pycomplexity
```

## Get started

Simple examples of using Big-O notation. Here are the most popular and common examples.

### Basic example

```python
from pycomplexity import BigO

big_o = BigO(full_report=True) # change to False if you need brief info

@big_o.complexity
def my_lovely_function():
    a = 1
    b = 2
    c = a + b
    return c
```

Console returns ``output``:

```
Function name: my_lovely_function
Function attributes: no attributes
-------------- BIG O --------------
Сomplexity of algorithm: O(1)
Memory of algorithm: O(1)
```

### Attributes vs Variables

Using ``arr`` as variable:

```python
from pycomplexity import BigO

big_o = BigO(full_report=False)

@big_o.complexity
def your_func():
    count = 0
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # fixed length
    for el in arr:
        count += el
    return count
```

Console returns ``output``:

```
Сomplexity of algorithm: O(1)
Memory of algorithm: O(1)
```

Using ``arr`` as attribute:

```python
from typing import List
from pycomplexity import BigO

big_o = BigO(full_report=False)

@big_o.complexity
def your_func(arr: List[int]) -> int:
    # not fixed length
    count = 0
    for el in arr:
        count += el
    return count
```

Console returns ``output``:

```
Сomplexity of algorithm: O(N)
Memory of algorithm: O(1)
```

## License

[MIT](http://opensource.org/licenses/MIT)

Copyright (c) 2023-present, Hagai