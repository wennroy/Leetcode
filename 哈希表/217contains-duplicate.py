class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # record = defaultdict(int)
        # for num in nums:
        #     record[num] += 1
        #     if record[num] > 1:
        #         return True
        # return False
        return len(nums) != len(set(nums))