# 简单模拟题
class Solution:
    def reformatNumber(self, number: str) -> str:
        s = list(map(str, number.replace(" ", "").replace("-", "")))
        n = len(s)
        count_3 = n // 3
        res_3 = n % 3
        if res_3 == 1 or res_3 == 0:
            count_3 -= 1
        for i in range(count_3, 0, -1):
            s[3 * i:3 * i] = ['-']
        if res_3 == 1:
            s[-2:-2] = ['-']

        return ''.join(s)

# 数组的插入，如果输入 s[-2:-2] = ['-'] 是在倒数第三的位置插入。