# Method signature checking decorator for Python 3

## Samples:

```python
from typecheck import *
```

```python
@typecheck
def foo(x: int, y: int) -> int:
    return x + y
```

You can describe error for error handling by scheme: `var: (type_or_checker, "error")`

```python
@typecheck
def method_with_error_handling(x: (int, "X must be integer, cool!") = 1, y: (str, 'Y must be string') = '') -> int:
    return x + int(y)
```

Checkers:
- optional
- with_attr
- by_regex 
- callable
- anything
- nothing
- tuple_of
- list_of
- set_of
- dict_of
- one_of 
- either
    
```python
@typecheck
def foo(x: int, y: int) -> int:
    return x + y
```

```python
@typecheck
def str_to_int(x: by_regex(r'[0-9]+')) -> int:
    return int(x)
```

```python
divisible_by_three = lambda x: x % 3 == 0
@typecheck
def str_to_int_divisible_by_3(i: by_regex("^[0-9]+$")) -> divisible_by_three:
    return int(i)
```



```python
@typecheck
def foo(i: int, x = None, s: str = "default") -> bool:
    ...
```

```python
@typecheck
def foo(*args, k1: int, k2: str = "default", k3 = None) -> nothing:
    ...
```

```python
@typecheck
def foo(ostream: with_attr("write", "flush"), f: optional(callable) = None):
    ...
```

```python
divisible_by_three = lambda x: x % 3 == 0
@typecheck
def foo(i: by_regex("^[0-9]+$")) -> divisible_by_three:
    ...
```

```python
@typecheck
def reverse_2_tuple(t: (str, bytes)) -> (bytes, str):
    ...
```

```python
@typecheck
def reverse_3_list(t: [int, float, bool]) -> [bool, float, int]:
    ...
```

```python
@typecheck
def extract_from_dict(d: dict_of(int, str), k: tuple_of(int)) -> list_of(str):
    ...
```

```python
@typecheck
def contains(x: int, xs: set_of(int)) -> bool:
    ...
```

```python
@typecheck
def set_level(level: one_of(1, 2, 3)):
    ...
```

```python
@typecheck
def accept_number(x: either(int, by_regex("^[0-9]+$"))):
    ...

```

```python
@typecheck_with_exceptions(input_parameter_error = MemoryError)
def custom_input_error(x: int): # now custom_input_error("foo") throws MemoryError
    ...
```

```python
@typecheck_with_exceptions(return_value_error = TypeError)
def custom_return_error() -> str: # now custom_return_error() throws TypeError
    return 1
```
