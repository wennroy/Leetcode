# 贪心，但边界条件，和选取条件总是没把握好
from collections import Counter
from sortedcontainers import SortedDict

class Solution:
    def largestPalindromic(self, num: str) -> str:
        num = list(map(int, num))
        cnt = Counter(num)
        odd_number = -1
        p_num = SortedDict()
        for number, count in cnt.most_common():
            if count % 2 == 0:
                p_num[number] = count
            elif odd_number == -1:
                p_num[number] = count
                odd_number = number
            elif odd_number < number:
                p_num[odd_number] -= 1
                if p_num[odd_number] == 0:
                    p_num.pop(odd_number)
                p_num[number] = count
                odd_number = number
            elif count > 1:
                p_num[number] = count - 1
        ans = ''
        middle_num = ''
        for l in p_num.keys()[::-1]:
            for _ in range(p_num[l] // 2):
                ans += str(l)
            if p_num[l] % 2 == 1:
                middle_num = str(l)

        if ans and ans[0] == '0':
            ans = ''
        ans = ans + middle_num + ans[::-1]

        return ans if ans else '0'


# 别人的贪心构造。
class Solution:
    def largestPalindromic(self, num: str) -> str:
        n = len(num)
        xf = Counter(num)

        mid = -1
        s = ''

        for x in range(9, -1, -1):
            c = str(x)
            s += (xf[c] // 2) * c
        for x in range(10):
            c = str(x)
            if xf[c] % 2 == 1:
                mid = x

        if mid != -1:
            res = s + str(mid) + s[::-1]
        else:
            res = s + s[::-1]

        res = res.lstrip('0').rstrip('0')
        if res:
            return res
        else:
            return '0'


# 作者：XingHe_XingHe
# 链接：https: // leetcode.cn / problems / largest - palindromic - number / solution / cpython3java - 1 - by - xinghe_xinghe - db0y /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。