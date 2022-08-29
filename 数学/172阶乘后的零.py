# O(n) 时间复杂度，寻找规律总结
class Solution:
    def find_how_many_5(self, x):
        if x % 5 != 0:
            return 0
        ans = 0
        while x and x % 5 == 0:
            ans += 1
            x //= 5
        return ans

    def trailingZeroes(self, n: int) -> int:
        # 观察发现，主要遇到含5的时候就会变成0（之前的乘子一定有偶数）
        # 遇到5的倍数多一位。25的倍数多两位。很容易接着往前推，也就是5**3多三倍这样子
        ans = 0
        for i in range(5,n+1,5):
            ans += self.find_how_many_5(i)
        return ans


