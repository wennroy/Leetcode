# 哈希表
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)

        n = len(nums)
        for num in nums:
            hash_table[num] += 1
            if hash_table[num] > n//2:
                return num

# moore 投票法
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/solution/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-pvh8/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。