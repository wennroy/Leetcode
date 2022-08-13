class Solution:
    def maxScore(self, s: str) -> int:
        from collections import Counter
        Cnt = Counter(s)
        if '1' not in Cnt.keys():
            return Cnt['0'] - 1
        elif '0' not in Cnt.keys():
            return Cnt['1'] - 1
        score_0, score_1 = 0, Cnt['1']
        ans = 0
        for letter in s[:-1]:
            if letter == '0':
                score_0 += 1
            else:
                score_1 -= 1
            cur_ans = score_0 + score_1
            if cur_ans > ans:
                ans = cur_ans

            if score_0 == Cnt["0"]:
                break

        return ans

class Solution:
    def maxScore(self, s: str) -> int:
        return max(s[:i].count('0') + s[i:].count('1') for i in range(1, len(s)))

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/maximum-score-after-splitting-a-string/solution/fen-ge-zi-fu-chuan-de-zui-da-de-fen-by-l-7u5p/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def maxScore(self, s: str) -> int:
        ans = score = (s[0] == '0') + s[1:].count('1')
        for c in s[1:-1]:
            score += 1 if c == '0' else -1
            ans = max(ans, score)
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/maximum-score-after-splitting-a-string/solution/fen-ge-zi-fu-chuan-de-zui-da-de-fen-by-l-7u5p/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。