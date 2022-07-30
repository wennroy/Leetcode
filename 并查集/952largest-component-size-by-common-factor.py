# 时间复杂度O(n^2)过不了
'''
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        from collections import defaultdict
        import math
        # O(n^2) 过不了
        nxt_pt_dict = defaultdict(list)
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                gcd_val = math.gcd(nums[i], nums[j])
                if gcd_val > 1:
                    nxt_pt_dict[i].append(j)
                    nxt_pt_dict[j].append(i)
        traveled = [0] * n
        max_ans = 0
        for i in range(n):
            if traveled[i] == 1:
                continue
            ans = 1
            stack = set()
            stack.add(i)
            while stack:
                ind = stack.pop()
                traveled[ind] = 1
                for nxt_pt in nxt_pt_dict[ind]:
                    if traveled[nxt_pt] == 0 and nxt_pt not in stack:
                        ans += 1
                        stack.add(nxt_pt)
            if ans > max_ans:
                max_ans = ans
        return max_ans

'''
# 并查集
# 利用值域来构建并查集
from collections import Counter


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x: int, y: int) -> None:
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        # 这里x的rank比y的rank来的大，因此我们选择让x成为y的父结点。
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            self.rank[x] += 1


class Solution:
    def largestComponentSize(self, nums: list[int]) -> int:
        uf = UnionFind(max(nums) + 1)
        for num in nums:
            i = 2
            while i * i <= num:
                if num % i == 0:
                    uf.merge(num, i)
                    uf.merge(num, num // i)
                i += 1
        return max(Counter(uf.find(num) for num in nums).values())


if __name__ == '__main__':
    nums = [4, 6, 15, 35]
    sol = Solution()
    print(sol.largestComponentSize(nums))