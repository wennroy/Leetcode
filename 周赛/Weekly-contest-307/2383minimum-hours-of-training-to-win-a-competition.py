# 俩dp
class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        n = len(energy)
        dp = [[0]*2 for _ in range(n)]
        dp[-1] = [energy[-1]+1, experience[-1]+1]
        for i in range(n-2, -1, -1):
            dp[i][0] = max(dp[i+1][0] + energy[i], energy[i]+1)
            dp[i][1] = max(dp[i+1][1] - experience[i], experience[i]+1)
        ans = max(dp[0][0] - initialEnergy,0) + max(dp[0][1] - initialExperience,0)
        return ans if ans > 0 else 0

# 贪心即可

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        need_exp = 0
        need_eng = max(sum(energy) + 1 - initialEnergy, 0)
        sum_exp = initialExperience
        for exp in experience:
            if exp < sum_exp:
                sum_exp += exp
            else:
                need_exp += exp - sum_exp + 1
                sum_exp = exp * 2 + 1
        return need_exp + need_eng

# 作者：SamLu
# 链接：https://leetcode.cn/problems/minimum-hours-of-training-to-win-a-competition/solution/by-samlu-qvhx/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。