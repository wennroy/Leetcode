# 经典的前缀和+队列处理
import collections
class Solution(object):
    def shortestSubarray(self, A, K):
        N = len(A)
        P = [0]
        for x in A:
            P.append(P[-1] + x)

        #Want smallest y-x with Py - Px >= K
        ans = N+1 # N+1 is impossible
        monoq = collections.deque() #opt(y) candidates, represented as indices of P
        for y, Py in enumerate(P):
            #Want opt(y) = largest x with Px <= Py - K
            while monoq and Py <= P[monoq[-1]]:
                monoq.pop()

            while monoq and Py - P[monoq[0]] >= K:
                ans = min(ans, y - monoq.popleft())

            monoq.append(y)

        return ans if ans < N+1 else -1

# 作者：LeetCode
# 链接：https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k/solution/he-zhi-shao-wei-k-de-zui-duan-zi-shu-zu-by-leetcod/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# 自己想的超时前缀和
from math import inf
class Solution(object):
    def shortestSubarray(self, A, K):
        n = len(A)
        pref = [0] * (n + 1)
        for i in range(1, n + 1):
            pref[i] = pref[i - 1] + A[i - 1]
        ans = n + 1

        for i in range(n + 1):
            for j in range(i + 1, min(i + ans + 1, n + 1)):
                if pref[j] - pref[i] >= K:
                    ans = min(ans, j - i)
                    break

        return ans if ans != n + 1 else -1