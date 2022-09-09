# 一次性扫描
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        flag = True
        while flag:
            i = len(ans)
            if i == len(strs[0]):
                ans += 'a'
                break
            cur_letter = strs[0][i]
            for s in strs:
                if i == len(s) or s[i] != cur_letter:
                    flag = False
                    break

            ans += cur_letter
        return ans[:-1]

# 横向扫描
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break

        return prefix

    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]

# 作者：LeetCode - Solution
# 链接：https: // leetcode.cn / problems / longest - common - prefix / solution / zui - chang - gong - gong - qian - zhui - by - leetcode - solution /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。