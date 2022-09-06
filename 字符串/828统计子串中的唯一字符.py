# 没看懂，等会儿再看看

# res += (arr[i] - arr[i - 1]) * (arr[i + 1] - arr[i])
# 从字符串的起始位置 (arr[i - 1], arr[i]] 到哦字符串的终止位置 [arr[i], arr[i+1]) 为止，总共有
# (arr[i] - arr[i - 1]) * (arr[i + 1] - arr[i])种组合包含这个字符。
import collections
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        index = collections.defaultdict(list)
        for i, c in enumerate(s):
            index[c].append(i)

        print(index)

        res = 0
        for arr in index.values():
            arr = [-1] + arr + [len(s)]
            for i in range(1, len(arr) - 1):
                res += (arr[i] - arr[i - 1]) * (arr[i + 1] - arr[i])
        return res