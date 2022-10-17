from functools import cache, lru_cache


@cache
def my_func(n, *args):
    print(args)
    return n + sum(list(args))

print(my_func(5,1,2,3,3))