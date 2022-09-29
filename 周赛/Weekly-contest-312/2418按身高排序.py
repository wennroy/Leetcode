# 简单题，sort一下解决
from typing import List
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        list_name = sorted(range(n), key=lambda x: -heights[x])
        ans = []
        for i in list_name:
            ans.append(names[i])

        return ans