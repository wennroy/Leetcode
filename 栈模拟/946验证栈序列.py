class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(pushed)
        stack = []
        i = j = 0
        while i < n:
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            stack.append(pushed[i])
            i += 1

        while stack and j < n and stack[-1] == popped[j]:
            stack.pop()
            j += 1

        if not stack:
            return True
        return False