# 哈希表记录，然后进行判断
# 条件部分比较麻烦。
from collections import defaultdict, Counter

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        cnt = Counter()
        cnt_num = defaultdict(int)
        ans = 0
        for i, num in enumerate(nums):
            if num not in cnt.keys():
                cnt.update([num])
            else:
                if cnt_num[cnt[num]] == 1:
                    cnt_num.pop(cnt[num])
                else:
                    cnt_num[cnt[num]] -= 1

                cnt.update([num])
            cnt_num[cnt[num]] += 1
            # 出现两种频率，最大的频率必只有一种数字或者频率1的数字只有一种数字。
            if len(cnt_num.keys()) == 2:
                if 1 in cnt_num.keys() and cnt_num[1] == 1:
                    ans = i + 1
                    continue
                a, b = sorted(cnt_num.keys())
                if b == a + 1 and cnt_num[b] == 1:
                    ans = i + 1
            # 只有一种数字，或者所有数字出现次数均为1成立
            elif len(cnt_num.keys()) == 1:
                if 1 in cnt_num.keys() or 1 in cnt_num.values():
                    ans = i + 1

        return ans


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        freq, count = Counter(), Counter()
        ans = maxFreq = 0
        for i, num in enumerate(nums):
            if count[num]:
                freq[count[num]] -= 1
            count[num] += 1
            maxFreq = max(maxFreq, count[num])
            freq[count[num]] += 1
            if maxFreq == 1 or \
               freq[maxFreq] * maxFreq + freq[maxFreq - 1] * (maxFreq - 1) == i + 1 and freq[maxFreq] == 1 or \
               freq[maxFreq] * maxFreq + 1 == i + 1 and freq[1] == 1:
                ans = max(ans, i + 1)
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/maximum-equal-frequency/solution/zui-da-xiang-deng-pin-lu-by-leetcode-sol-5y2m/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。