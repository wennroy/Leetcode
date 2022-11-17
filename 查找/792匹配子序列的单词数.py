from collections import defaultdict, deque
from bisect import bisect_right
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        record = defaultdict(deque)
        for i, val in enumerate(s):
            record[val].append(i)
        ans = 0
        for word in words:
            min_idx = -1
            flag = True
            for i, val in enumerate(word):
                if val not in record.keys():
                    flag = False
                    break
                idx = bisect_right(record[val], min_idx)
                if idx == len(record[val]):
                    flag = False
                    break
                min_idx = record[val][idx]

            if flag:
                ans += 1

        return ans


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        pos = defaultdict(list)
        for i, c in enumerate(s):
            pos[c].append(i)
        ans = len(words)
        for w in words:
            if len(w) > len(s):
                ans -= 1
                continue
            p = -1
            for c in w:
                ps = pos[c]
                j = bisect_right(ps, p)
                if j == len(ps):
                    ans -= 1
                    break
                p = ps[j]
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/number-of-matching-subsequences/solution/pi-pei-zi-xu-lie-de-dan-ci-shu-by-leetco-vki7/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。