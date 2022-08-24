# 直接递归

NUMS = list(range(10))
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        if n == 1:
            return NUMS[1:]
        res = self.printNumbers(n - 1)
        ans = []
        for num in NUMS[1:]:
            ans.append(num)
        for num in res:
            for last_digit in NUMS:
                ans.append(num * 10 + last_digit)

        return ans