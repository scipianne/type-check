[![PyPI](https://img.shields.io/pypi/v/type-check.svg)](https://pypi.org/project/type-check/)

# Type Check
Type check decorator for python

## Installation:

```
pip3 install type-check
```

## Usage:

Import `type_check` decorator:

```
from type_check import type_check
```

Usage in function:

```
@type_check()
def my_func(arg: type = default) -> return_type:
    pass
```

At class function, specify type of `self` with base type, for example:

```
def __init__(self: object, arg: type = default):
    pass
```
