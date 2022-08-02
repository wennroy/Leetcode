import timeit
from functools import lru_cache
cnt = 0
def fib(n):
    if n == 1:
        global cnt
        cnt += 1
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

if __name__=="__main__":

    cnt = 0
    print(timeit.timeit('fib(36)', number=1, globals=globals()))
    print("fib(1) 调用次数：%d" % cnt)

    cnt = 0

    @lru_cache(maxsize=None, typed=False)
    def fib(n):
        if n == 1:
            global cnt
            cnt += 1
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

    print(timeit.timeit('fib(36)', number=1, globals=globals()))
    print("fib(1) 调用次数：%d" % cnt)
    print(fib.cache_info())  # 查看缓存信息