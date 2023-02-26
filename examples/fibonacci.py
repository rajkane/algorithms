from functools import wraps
import time


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__} {args} {kwargs} Took {total_time:.8f} seconds')
        return result
    return timeit_wrapper


@timeit
def fib_recursive(n: int):
    """ recursion fibonacci sequence function """
    return n if n <= 1 else fib_recursive(n - 1) + fib_recursive(n - 2)


cache = {0: 0, 1: 1}
@timeit
def fib_memoize(n: int):
    """ memoization fibonacci sequence function """
    if n in cache:
        return cache[n]
    cache[n] = fib_memoize(n - 1) + fib_memoize(n - 2)
    return cache[n]

@timeit
def fib_iter(n: int):
    """ iteration fibonacci sequence function """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    print("""
    Select: 
    1) Recursion
    2) Memotization
    3) Iteration
    """)
    print("-----------------------------")
    i = input("Enter function: ")
    n = input("Enter n number: ")
    print("-----------------------------")

    i, n = int(i), int(n)
    if i == 1:
        result = [fib_recursive(j) for j in range(n)]
    elif i == 2:
        result = [fib_memoize(j) for j in range(n)]
    elif i == 3:
        result = [fib_iter(j) for j in range(n)]
    else:
        result = "Undefined"

    print(result)
