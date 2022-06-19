class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        pt = 0
        n = len(arr)
        new_n = n
        while pt < n:
            if arr[pt] == 0:
                arr.insert(pt, 0)
                pt += 1
                new_n += 1
            pt += 1
        for i in range(n, new_n):
            arr.pop()

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n = len(arr)
        top = 0
        i = -1
        while top < n:
            i += 1
            top += 1 if arr[i] else 2
        j = n - 1
        if top == n + 1:
            arr[j] = 0
            j -= 1
            i -= 1
        while j >= 0:
            arr[j] = arr[i]
            j -= 1
            if arr[i] == 0:
                arr[j] = arr[i]
                j -= 1
            i -= 1
'''
作者：LeetCode-Solution
链接：https://leetcode.cn/problems/duplicate-zeros/solution/fu-xie-ling-by-leetcode-solution-7ael/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''