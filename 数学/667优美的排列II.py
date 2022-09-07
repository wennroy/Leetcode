# 从 k = n-1的情况开始generalize出来的结果。

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = []
        l, r = 1, n
        is_left = True
        while k > 1:
            if is_left:
                ans.append(l)
                l += 1
                is_left = False
            else:
                ans.append(r)
                r -= 1
                is_left = True
            k -= 1

        if is_left:
            for i in range(l, r + 1):
                ans.append(i)
        else:
            for i in range(r, l - 1, -1):
                ans.append(i)

        return ans

# 标答方法：基本一致，只不过他把“左右互搏”放在了后面
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        answer = list(range(1, n - k))
        i, j = n - k, n
        while i <= j:
            answer.append(i)
            if i != j:
                answer.append(j)
            i, j = i + 1, j - 1
        return answer

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/beautiful-arrangement-ii/solution/you-mei-de-pai-lie-ii-by-leetcode-soluti-qkrs/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。