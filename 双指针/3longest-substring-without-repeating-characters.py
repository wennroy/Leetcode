# 改良版双指针，利用list速度较慢
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        x, y, ans = 0, 0, 0
        for x in range(n):
            if x == 0:
                record_list = []
            else:
                record_list.remove(s[x-1])
            while y < n and not s[y] in record_list:
                record_list.append(s[y])
                y += 1
            if y-x > ans:
                ans = y-x
        return ans

# 第一版双指针
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        x, y, ans = 0, 0, 0
        for x in range(n):
            if x == 0:
                record_list = [s[0]]
            else:
                del(record_list[0])
            while y < n and not s[y] in record_list:
                record_list.append(s[y])
                y += 1
            if y-x+1 > ans:
                ans = y-x+1
            # print(record_list)
        return ans

# 双指针
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans

'''
标答快了30ms 92 -> 60
将list -> set
作者：LeetCode-Solution
链接：https://leetcode.cn/problems/longest-substring-without-repeating-characters/solution/wu-zhong-fu-zi-fu-de-zui-chang-zi-chuan-by-leetc-2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''