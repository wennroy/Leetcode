# 各种细节的小问题，一些值域的选择都需要注意
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort(reverse=True)
        wild_card = 0
        while nums and nums[-1] == 0:
            nums.pop()
            wild_card += 1
        if not nums:  # 五张大小王
            return True

        if len(nums) > len(set(nums)):
            return False

        min_val, max_val = nums[-1], nums[0]
        if max_val > min_val + 4:  # 超过5的范围不可能有顺子
            return False

        for i in range(min_val + 1, max_val):
            if not i in nums:
                wild_card -= 1

        if wild_card < 0:
            return False

        return True

# 差不多是一个思路，但我写的略微麻烦
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        repeat = set()
        ma, mi = 0, 14
        for num in nums:
            if num == 0: continue # 跳过大小王
            ma = max(ma, num) # 最大牌
            mi = min(mi, num) # 最小牌
            if num in repeat: return False # 若有重复，提前返回 false
            repeat.add(num) # 添加牌至 Set
        return ma - mi < 5 # 最大牌 - 最小牌 < 5 则可构成顺子

# 作者：jyd
# 链接：https://leetcode.cn/problems/bu-ke-pai-zhong-de-shun-zi-lcof/solution/mian-shi-ti-61-bu-ke-pai-zhong-de-shun-zi-ji-he-se/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。