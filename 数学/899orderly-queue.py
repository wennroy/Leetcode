# 脑筋急转弯题目

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            ans = s
            for _ in range(len(s) - 1):
                s = s[1:] + s[0]
                ans = min(ans, s)
            return ans
        return ''.join(sorted(s))


# 当 k = 1的时候，就只能按照字符串本身的顺序移动，因此找到最小的那个字符在队首，此时就是答案
# 当 k = 2的时候，我们就能够像冒泡排序一样，每次在将两个字符排列到队首，交换他们的顺序到队尾，重复操作，直到排序完成。
# 因此当 k>=2 的时候，我们总能得到有序排列。