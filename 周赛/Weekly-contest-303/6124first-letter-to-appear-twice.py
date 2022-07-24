# 送分简单题
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        record = [0] * 26
        for a in s:
            idx = ord(a) - ord('a')
            record[idx] += 1
            if record[idx] == 2:
                return a