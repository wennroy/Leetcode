# 哈希表
from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hash_table = defaultdict(list)
        ans = []
        for idx, val in enumerate(groupSizes):
            hash_table[val].append(idx)
            if len(hash_table[val]) == val:
                tmp = hash_table.pop(val)
                ans.append(tmp)

        return ans