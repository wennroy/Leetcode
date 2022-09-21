# 哈希表
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        n, m = len(arr), len(pieces)
        first_num = dict()
        for j in range(m):
            first_num[pieces[j][0]] = j
        i = 0
        while i < n:
            if arr[i] not in first_num.keys():
                return False
            for num in pieces[first_num[arr[i]]]:
                if num == arr[i]:
                    i += 1
                else:
                    return False

        return True