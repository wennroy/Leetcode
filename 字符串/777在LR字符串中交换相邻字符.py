# 高端解法
class Solution:
    def canTransform(self, start: str, target: str) -> bool:
        if start.replace('X', '') != target.replace('X', ''):
            return False
        j = 0
        for i, c in enumerate(start):
            if c == 'X':
                continue
            while target[j] == 'X':
                j += 1
            if i != j and (c == 'L') != (i > j):
                return False
            j += 1
        return True

# 作者：endlesscheng
# 链接：https://leetcode.cn/problems/swap-adjacent-in-lr-string/solution/by-endlesscheng-fcgc/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 标答的双指针
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        n = len(start)
        i = j = 0
        while i < n and j < n:
            while i < n and start[i] == 'X':
                i += 1
            while j < n and end[j] == 'X':
                j += 1
            if i < n and j < n:
                if start[i] != end[j]:
                    return False
                c = start[i]
                if c == 'L' and i < j or c == 'R' and i > j:
                    return False
                i += 1
                j += 1
        while i < n:
            if start[i] != 'X':
                return False
            i += 1
        while j < n:
            if end[j] != 'X':
                return False
            j += 1
        return True

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/swap-adjacent-in-lr-string/solution/zai-lrzi-fu-chuan-zhong-jiao-huan-xiang-rjaw8/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
