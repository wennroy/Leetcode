# 方法一：动态规划，斐波那契数列
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2,n):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[-1]

# 方法二：矩阵快速幂
# public class Solution {
#     public int climbStairs(int n) {
#         int[][] q = {{1, 1}, {1, 0}};
#         int[][] res = pow(q, n);
#         return res[0][0];
#     }
#
#     public int[][] pow(int[][] a, int n) {
#         int[][] ret = {{1, 0}, {0, 1}};
#         while (n > 0) {
#             if ((n & 1) == 1) {
#                 ret = multiply(ret, a);
#             }
#             n >>= 1;
#             a = multiply(a, a);
#         }
#         return ret;
#     }
#
#     public int[][] multiply(int[][] a, int[][] b) {
#         int[][] c = new int[2][2];
#         for (int i = 0; i < 2; i++) {
#             for (int j = 0; j < 2; j++) {
#                 c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j];
#             }
#         }
#         return c;
#     }
# }
#
# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# 方法三：通项公式
# public class Solution {
#     public int climbStairs(int n) {
#         double sqrt5 = Math.sqrt(5);
#         double fibn = Math.pow((1 + sqrt5) / 2, n + 1) - Math.pow((1 - sqrt5) / 2, n + 1);
#         return (int) Math.round(fibn / sqrt5);
#     }
# }
#
# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。