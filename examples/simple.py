from typecheck import *
from time import time
from typecheck import has_error


@typecheck
def foo(x: int, y: int) -> int:
    return x + y


@typecheck_with_exceptions(input_parameter_error=TypeCheckError)
def str_to_int(x: by_regex(r'[0-9]+')) -> int:
    return int(x)


divisible_by_three = lambda x: x % 3 == 0


@typecheck
def str_to_int_divisible_by_3(i: by_regex("^[0-9]+$")) -> divisible_by_three:
    return int(i)


@typecheck
def method_with_error_handling(x: (int, "X must be integer, cool!") = 1, y: (str, 'Y must be string') = '') -> int:
    return x + int(y)


# Divisible() delete all checks
start = time()
disable()  # comment it
for i in range(1000):
    print(foo(2, 3))
    print(str_to_int('3'))
    print(str_to_int_divisible_by_3('9'))
print(time() - start)

print(method_with_error_handling(y="23"))
