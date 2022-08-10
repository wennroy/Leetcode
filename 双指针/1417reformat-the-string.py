# 双指针
class Solution:
    def reformat(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        pt = 0
        num_ans, str_ans = [], []
        while pt < n:
            if ord('0') <= ord(s[pt]) <= ord('9'):
                num_ans.append(s[pt])
            else:
                str_ans.append(s[pt])
            pt += 1

        m, n = len(num_ans), len(str_ans)
        if abs(m - n) > 1:
            return ''

        if m >= n:
            first, second = num_ans, str_ans
        else:
            first, second = str_ans, num_ans
        ans = []
        i = 0
        while i < min(n, m):
            ans.append(first[i])
            ans.append(second[i])
            i += 1
        if i < max(n, m):
            ans.append(first[i])
        return ''.join(ans)

# 更为优秀的双指针
class Solution:
    def reformat(self, s: str) -> str:
        sumDigit = sum(c.isdigit() for c in s)
        sumAlpha = len(s) - sumDigit
        if abs(sumDigit - sumAlpha) > 1:
            return ""
        flag = sumDigit > sumAlpha
        t = list(s)
        j = 1
        for i in range(0, len(t), 2):
            if t[i].isdigit() != flag:
                while t[j].isdigit() != flag:
                    j += 2
                t[i], t[j] = t[j], t[i]
        return ''.join(t)

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/reformat-the-string/solution/zhong-xin-ge-shi-hua-zi-fu-chuan-by-leet-lgqx/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。