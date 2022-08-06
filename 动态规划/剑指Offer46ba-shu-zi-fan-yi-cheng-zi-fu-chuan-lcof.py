class Solution:
    def isTwoways(self, a: int, b: int) -> bool:
        if a == 1 or a == 2 and b < 6:
            return True
        else:
            return False

    def translateNum(self, num: int) -> int:
        num = str(num)
        n = len(num)
        first, second = 1, 1
        for i in range(1, n):
            if self.isTwoways(int(num[i - 1]), int(num[i])):
                third = first + second
            else:
                third = second

            first = second
            second = third

        return third if n >= 2 else 1


class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        a = b = 1
        for i in range(2, len(s) + 1):
            a, b = (a + b if "10" <= s[i - 2:i] <= "25" else a), a
        return a

# 作者：jyd
# 链接：https://leetcode.cn/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/solution/mian-shi-ti-46-ba-shu-zi-fan-yi-cheng-zi-fu-chua-6/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。