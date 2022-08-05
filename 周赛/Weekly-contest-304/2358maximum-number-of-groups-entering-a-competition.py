class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        x = 1
        while x*(x-1) < 2*n:
            x += 1
        if x*(x-1) == 2*n:
            return x - 1
        else:
            return x - 2