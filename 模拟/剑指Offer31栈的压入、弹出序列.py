# 由于数字不同，我们可以直接模拟一个栈
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if not pushed:
            return True
        push_pt, pop_pt = 1, 0
        stack = [pushed[0]]
        n = len(pushed)
        while push_pt < n:
            if not stack or stack[-1] != popped[pop_pt]:
                stack.append(pushed[push_pt])
                push_pt += 1
            else:
                stack.pop()
                pop_pt += 1
        if stack[::-1] == popped[pop_pt:]:
            return True
        return False

# 由于num一定会入栈，可以考虑直接循环pushed，然后遇到在出栈。栈最后为空则成功
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, i = [], 0
        for num in pushed:
            stack.append(num) # num 入栈
            while stack and stack[-1] == popped[i]: # 循环判断与出栈
                stack.pop()
                i += 1
        return not stack

# 作者：jyd
# 链接：https://leetcode.cn/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/solution/mian-shi-ti-31-zhan-de-ya-ru-dan-chu-xu-lie-mo-n-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。