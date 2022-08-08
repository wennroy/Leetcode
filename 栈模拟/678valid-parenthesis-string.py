# 方法一： 遍历 从左遍历确保左括号可行，从右遍历确保右括号可行，均可行则通过示例
class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        cnt_left = cnt_star = 0
        for i, val in enumerate(s):
            if val == '(':
                cnt_left += 1
            elif val == '*':
                cnt_star += 1

            if val == ')':
                if cnt_left == 0 and cnt_star == 0:
                    return False
                elif cnt_left != 0:
                    cnt_left -= 1
                else:
                    cnt_star -= 1

        if (cnt_star - cnt_left) < 0:
            return False

        cnt_right = cnt_star = 0

        for i, val in enumerate(s[::-1]):
            if val == ')':
                cnt_right += 1
            elif val == '*':
                cnt_star += 1

            if val == '(':
                if cnt_right == 0 and cnt_star == 0:
                    return False
                elif cnt_right != 0:
                    cnt_right -= 1
                else:
                    cnt_star -= 1

        return True


# 一年前的我真牛逼，栈解法。
# 又看不懂我写了啥了？？

class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            cur_str = s[i]
            if cur_str == '(' or cur_str == '*':
                stack.append(cur_str)
            elif cur_str == ')':
                if not stack:
                    return False

                ifdel = False
                for k in range(len(stack) - 1, -1, -1):
                    if stack[k] == '(':
                        del stack[k]
                        ifdel = True
                        break

                if not ifdel:
                    stack.pop()

        print(stack)
        if stack == []:
            return True
        new_stack = []
        new_stack.append(stack.pop())

        if new_stack[0] == '(':
            return False

        while stack:
            cur_str = stack.pop()
            if cur_str == '(':
                if not new_stack:
                    return False
                else:
                    new_stack.pop()
            else:
                new_stack.append(cur_str)
        return True

# 动态规划
'''
class Solution {
    public boolean checkValidString(String s) {
        int n = s.length();
        boolean[][] dp = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == '*') {
                dp[i][i] = true;
            }
        }
        for (int i = 1; i < n; i++) {
            char c1 = s.charAt(i - 1), c2 = s.charAt(i);
            dp[i - 1][i] = (c1 == '(' || c1 == '*') && (c2 == ')' || c2 == '*');
        }
        for (int i = n - 3; i >= 0; i--) {
            char c1 = s.charAt(i);
            for (int j = i + 2; j < n; j++) {
                char c2 = s.charAt(j);
                if ((c1 == '(' || c1 == '*') && (c2 == ')' || c2 == '*')) {
                    dp[i][j] = dp[i + 1][j - 1];
                }
                for (int k = i; k < j && !dp[i][j]; k++) {
                    dp[i][j] = dp[i][k] && dp[k + 1][j];
                }
            }
        }
        return dp[0][n - 1];
    }
}
'''
# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/valid-parenthesis-string/solution/you-xiao-de-gua-hao-zi-fu-chuan-by-leetc-osi3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 标答的栈
'''
class Solution {
    public boolean checkValidString(String s) {
        Deque<Integer> leftStack = new LinkedList<Integer>();
        Deque<Integer> asteriskStack = new LinkedList<Integer>();
        int n = s.length();
        for (int i = 0; i < n; i++) {
            char c = s.charAt(i);
            if (c == '(') {
                leftStack.push(i);
            } else if (c == '*') {
                asteriskStack.push(i);
            } else {
                if (!leftStack.isEmpty()) {
                    leftStack.pop();
                } else if (!asteriskStack.isEmpty()) {
                    asteriskStack.pop();
                } else {
                    return false;
                }
            }
        }
        while (!leftStack.isEmpty() && !asteriskStack.isEmpty()) {
            int leftIndex = leftStack.pop();
            int asteriskIndex = asteriskStack.pop();
            if (leftIndex > asteriskIndex) {
                return false;
            }
        }
        return leftStack.isEmpty();
    }
}

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/valid-parenthesis-string/solution/you-xiao-de-gua-hao-zi-fu-chuan-by-leetc-osi3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''