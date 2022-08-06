# 滑动窗口，最快44ms，击败99%

from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        visited = defaultdict(lambda :-1)
        max_len = 0
        start_pos = 0
        for i in range(n):
            val = s[i]
            if visited[val] == -1:
                visited[val] = i
            else:
                if start_pos > visited[val]:
                    visited[val] = i
                    continue
                if max_len < i - start_pos:
                    max_len = i - start_pos
                start_pos = visited[val] + 1
                visited[val] = i
        return max_len if i - start_pos + 1 < max_len else i - start_pos + 1


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = tmp = 0
        for j in range(len(s)):
            i = dic.get(s[j], -1) # 获取索引 i
            dic[s[j]] = j # 更新哈希表
            tmp = tmp + 1 if tmp < j - i else j - i # dp[j - 1] -> dp[j]
            res = max(res, tmp) # max(dp[j - 1], dp[j])
        return res

# 作者：jyd
# 链接：https://leetcode.cn/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/solution/mian-shi-ti-48-zui-chang-bu-han-zhong-fu-zi-fu-d-9/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。