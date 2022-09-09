# 超时 时间复杂度最差要O(n*m) m是值域最大值
class Solution:
    def trap(self, height: List[int]) -> int:
        # val 值域作为dp
        dp = [-1] * 10**5
        ans = 0
        for ind, num in enumerate(height):
            for i in range(num):
                if dp[i] != -1:
                    ans += ind - dp[i] - 1
                dp[i] = ind

        return ans

# 方法一：动态规划，寻找共同的覆盖面积
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        LeftMax, RightMax = [0] * n, [0] * n
        LeftMax[-1] = height[-1]
        RightMax[0] = height[0]
        for i in range(n - 2, -1, -1):
            LeftMax[i] = max(height[i], LeftMax[i + 1])
        for i in range(1, n):
            RightMax[i] = max(height[i], RightMax[i - 1])

        ans = 0
        for i in range(n):
            ans += min(LeftMax[i], RightMax[i]) - height[i]

        return ans

# 方法二：单调栈

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = list()
        n = len(height)

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                currWidth = i - left - 1
                currHeight = min(height[left], height[i]) - height[top]
                ans += currWidth * currHeight
            stack.append(i)

        return ans