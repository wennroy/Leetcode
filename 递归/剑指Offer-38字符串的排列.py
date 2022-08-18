from functools import cache
class Solution:
    @cache
    def permutation(self, s: str) -> List[str]:
        n = len(s)
        if n == 1:
            return [s]
        ans = set()
        for i in range(n):
            for last_ans in self.permutation(s[:i] + s[i+1:]):
                ans.add(s[i]+last_ans)
        return list(ans)