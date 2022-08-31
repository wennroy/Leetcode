# 直接遍历 On^2
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        RightMax = [0] * n
        RightMax[n - 1] = prices[-1]
        for i in range(n - 2, -1, -1):
            RightMax[i] = max(RightMax[i + 1], prices[i])

        for i in range(n):
            if prices[i] > RightMax[i]:
                continue
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break

        return prices

# 反过来的单调栈

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        ans = [0] * n
        st = [0]
        for i in range(n - 1, -1, -1):
            p = prices[i]
            while len(st) > 1 and st[-1] > p:
                st.pop()
            ans[i] = p - st[-1]
            st.append(p)
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/final-prices-with-a-special-discount-in-a-shop/solution/shang-pin-zhe-kou-hou-de-zui-zhong-jie-g-ind3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。