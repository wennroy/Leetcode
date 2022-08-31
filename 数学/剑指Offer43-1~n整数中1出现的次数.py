# 反复调试强算。耗时大概快一个小时
# 一半的时间都在debug，最后**少写了一个*，气死


class Solution:
    def countDigitOne(self, n: int) -> int:
        str_n = str(n)
        num_digits = len(str_n)
        ans = 0
        for i, l in enumerate(str_n):
            if i==0:
                if int(l) > 1:
                    ans += 1 * 10**(num_digits-1)
                elif num_digits == 1:
                    return 1 if n > 0 else 0
                else:
                    ans += int(str_n[1:]) + 1
            elif i == num_digits-1:
                ans += int(str_n[:-1])
                if int(l) >= 1:
                    ans += 1
            else:
                ans += (int(str_n[:i])) * 10**(num_digits-i-1)
                if int(l) > 1:
                    ans += 10**(num_digits-i-1)
                elif int(l) == 1:
                    ans += int(str_n[i+1:])+1
        return ans


class Solution:
    def countDigitOne(self, n: int) -> int:
        # mulk 表示 10^k
        # 在下面的代码中，可以发现 k 并没有被直接使用到（都是使用 10^k）
        # 但为了让代码看起来更加直观，这里保留了 k
        k, mulk = 0, 1
        ans = 0
        while n >= mulk:
            ans += (n // (mulk * 10)) * mulk + min(max(n % (mulk * 10) - mulk + 1, 0), mulk)
            k += 1
            mulk *= 10
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/solution/1n-zheng-shu-zhong-1-chu-xian-de-ci-shu-umaj8/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。