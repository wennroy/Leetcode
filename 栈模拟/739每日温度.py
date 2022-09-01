# 暴力遍历
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        record = [-1] * (100 - 30 + 1)
        ans = [n] * n
        for i in range(n - 1, -1, -1):
            cur_temp = temperatures[i]
            for j in range(cur_temp + 1, 101):
                j -= 30
                if record[j] > i and record[j] != -1:
                    ans[i] = min(ans[i], record[j] - i)
            if ans[i] == n:
                ans[i] = 0
            record[cur_temp - 30] = i

        return ans

# 单调栈
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            while stack:
                val, idx = stack.pop()
                if val > temperatures[i]:
                    ans[i] = idx - i
                    stack.append((val, idx))
                    break

            if not stack:
                ans[i] = 0
            stack.append((temperatures[i], i))

        return ans

# 标答单调栈
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        ans = [0] * length
        stack = []
        for i in range(length):
            temperature = temperatures[i]
            while stack and temperature > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans
#
# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/daily-temperatures/solution/mei-ri-wen-du-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。