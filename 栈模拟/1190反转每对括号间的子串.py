# 暴力栈，居然过了
class Solution:
    def reverseParentheses(self, s: str) -> str:
        if not s:
            return ""
        stack = []
        n = len(s)
        s_list = list(s)
        for i in range(n):
            if s_list[i] == '(':
                stack.append(i)

            elif s_list[i] == ')':
                j = stack.pop()
                s_list[j + 1:i] = s_list[i - 1:j:-1]
        s = ''.join(s_list)
        s = s.replace('(', '')
        s = s.replace(')', '')
        return s

# 预处理括号
'''
class Solution {
public:
    string reverseParentheses(string s) {
        int n = s.length();
        vector<int> pair(n);
        stack<int> stk;
        for (int i = 0; i < n; i++) {
            if (s[i] == '(') {
                stk.push(i);
            } else if (s[i] == ')') {
                int j = stk.top();
                stk.pop();
                pair[i] = j, pair[j] = i;
            }
        }

        string ret;
        int index = 0, step = 1;
        while (index < n) {
            if (s[index] == '(' || s[index] == ')') {
                index = pair[index];
                step = -step;
            } else {
                ret.push_back(s[index]);
            }
            index += step;
        }
        return ret;
    }
};

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/reverse-substrings-between-each-pair-of-parentheses/solution/fan-zhuan-mei-dui-gua-hao-jian-de-zi-chu-gwpv/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

# 逆序遍历字符串

class Solution:
    def reverseParentheses(self, s: str) -> str:
        if not s:
            return ""
        brackets = dict()

        n = len(s)
        stack = []
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                val = stack.pop()
                brackets[val] = i
                brackets[i] = val

        i = 0
        ans = []
        DIR = 1
        while i < n:
            if s[i] not in ['(', ')']:
                ans.append(s[i])
            else:
                i = brackets[i]
                DIR *= -1
            i += DIR
        return ''.join(ans)