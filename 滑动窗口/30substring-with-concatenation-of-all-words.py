# 超时写法
#
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        '''
        1. 找到word in words 每个词的起始位置，利用record字典记录下来 （哈希表）
            import re
            [m.start() for m in re.finditer('test', 'test test test test')]
            #[0, 5, 10, 15]


        2. 对每一个word的起始位置进行判断，寻找能串联的可能性 （DFS寻找 再建立一个traveled列表来记录是否访问word）
        3. 最终返回成立的串联起始位置
        '''

        def find_all(a_str, sub):
            start = 0
            while True:
                start = a_str.find(sub, start)
                if start == -1:
                    return
                yield start  # https://www.runoob.com/w3cnote/python-yield-used-analysis.html
                start += 1  # use start += 1 to find overlapping matches

        record = {}
        for word in words:
            record[word] = list(find_all(s, word))

        word_len = len(words[0])

        # print(record)

        def dfs(cur_step, traveled, word_len):
            # print(cur_step, traveled)
            if sum(traveled) == len(traveled):
                return True
            for word, start_list in record.items():
                for ind, val in enumerate(words):
                    if val == word and traveled[ind] == 0 and cur_step in start_list:
                        traveled[ind] = 1
                        ans = dfs(cur_step + word_len, traveled, word_len)
                        if not ans:
                            traveled[ind] = 0
                        if ans:
                            return True
            return False

        ans = []

        for start in range(len(s) - word_len * len(words) + 1):
            traveled = [0] * len(words)
            if dfs(start, traveled, word_len):
                ans.append(start)
        return ans

# 标答使用滑动窗口
from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        m, n, ls = len(words), len(words[0]), len(s)
        for i in range(n):
            if i + m * n > ls:
                break
            differ = Counter()
            for j in range(m):
                word = s[i + j * n: i + (j + 1) * n]
                differ[word] += 1
            for word in words:
                differ[word] -= 1
                if differ[word] == 0:
                    del differ[word]
            for start in range(i, ls - m * n + 1, n):
                if start != i:
                    word = s[start + (m - 1) * n: start + m * n]
                    differ[word] += 1
                    if differ[word] == 0:
                        del differ[word]
                    word = s[start - n: start]
                    differ[word] -= 1
                    if differ[word] == 0:
                        del differ[word]
                if len(differ) == 0:
                    res.append(start)
        return res
'''
作者：LeetCode-Solution
链接：https://leetcode.cn/problems/substring-with-concatenation-of-all-words/solution/chuan-lian-suo-you-dan-ci-de-zi-chuan-by-244a/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''