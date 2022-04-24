import cProfile
import math
import pstats
from functools import cache, lru_cache


def main():
    # Use a breakpoint in the code line below to debug your script.
    functions = [fib, cached_fib, max_sized_cached_fib, reduced_fib]

    for function in functions:
        print(f"Running function {function.__name__!r}")
        if function.__name__ == 'fib':
            maximum = 35
        else:
            maximum = 400
        with cProfile.Profile() as pr:
            for n in range(maximum):
                print(f'with {n=} {function.__name__}: {function(n)}')

        stats = pstats.Stats(pr)
        stats.sort_stats(pstats.SortKey.TIME)
        stats.print_stats()
        stats.dump_stats(f'math_{function.__name__}.prof')


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


@cache
def cached_fib(n):
    if n <= 1:
        return n
    return cached_fib(n - 1) + cached_fib(n - 2)


@lru_cache(maxsize=5)
def max_sized_cached_fib(n):
    if n <= 1:
        return n
    return max_sized_cached_fib(n - 1) + max_sized_cached_fib(n - 2)


def reduced_fib(n):
    """
    mathematically correct but imprecise because of floating point arithmatic and limited memory
    """
    fsqrt = math.sqrt(5)
    return (1 / fsqrt) * ((((1 + fsqrt) / 2) ** n) - (((1 - fsqrt) / 2) ** n))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
