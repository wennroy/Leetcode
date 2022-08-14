# O(n) O(1)
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        cur_num = 1
        cur_D = 0
        ans = ''
        for i in range(len(pattern)):
            cur_move = pattern[i]
            if cur_move == 'I':
                ans += str(cur_num)
                tmp = cur_num
                while cur_D > 0:
                    cur_D -= 1
                    tmp -= 1
                    ans += str(tmp)
            else:
                cur_D += 1
            cur_num += 1
        cur_num += 1
        cur_D += 1
        while cur_D > 0:
            cur_D -= 1
            cur_num -= 1
            ans += str(cur_num)
        return ans