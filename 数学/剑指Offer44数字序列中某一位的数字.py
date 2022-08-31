class Solution:
    def findNthDigit(self, n: int) -> int:
        if n == 0:
            return 0
        # 9 + 90*2 + 900*3
        digits = sum_digit = 0
        last_sum = 0
        while sum_digit < n:
            digits += 1
            last_sum = sum_digit
            sum_digit += 9*10**(digits-1)*digits
        if digits != 1:
            val = (n-last_sum) // digits + 10**(digits-1)
        else:
            return n
        res = (n-last_sum) % digits
        if res == 0:
            return int(str(val-1)[-1])
        else:
            return int(str(val)[res-1])



class Solution:
    def findNthDigit(self, n: int) -> int:
        digit, start, count = 1, 1, 9
        while n > count: # 1.
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        num = start + (n - 1) // digit # 2.
        return int(str(num)[(n - 1) % digit]) # 3.

# 作者：jyd
# 链接：https://leetcode.cn/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/solution/mian-shi-ti-44-shu-zi-xu-lie-zhong-mou-yi-wei-de-6/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。