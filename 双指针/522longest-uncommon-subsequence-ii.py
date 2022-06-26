# 标答版本
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_substr(s, t):
            pt_s = pt_t = 0
            while pt_s < len(s) and pt_t < len(t):
                if s[pt_s] == t[pt_t]:
                    pt_s += 1
                pt_t += 1
            return pt_s == len(s)

        ans = -1
        for i, s in enumerate(strs):
            check = True
            for j, t in enumerate(strs):
                if i != j and is_substr(s,t):
                    check = False
                    break

            if check:
                ans = max(ans, len(s))
        return ans


# 先行整理，从大到小排列，以节省时间

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        ban = set()
        s = set()
        for i in strs:
            if i not in s:
                s.add(i)
            else:
                ban.add(i)
        for i in ban:
            s.remove(i)

        def substring(a, b):
            cur = 0
            i = 0
            while cur < len(a) and i < len(b):
                if b[i] == a[cur]:
                    cur += 1
                i += 1
            return cur == len(a)

        def check(i):
            for j in ban:
                if substring(i, j):
                    return False
            return True

        s = sorted(list(s), key=lambda x: len(x), reverse=True)
        for i in s:
            if check(i):
                return len(i)
        return -1


'''
作者：qian-li-ma-8
链接：https://leetcode.cn/problems/longest-uncommon-subsequence-ii/solution/by-qian-li-ma-8-nb60/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
