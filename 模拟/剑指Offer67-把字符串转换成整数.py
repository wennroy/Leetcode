# 状态自动机

RANGE = [-2 ** 31, 2 ** 31 - 1]
from enum import Enum


class Solution:
    def strToInt(self, str: str) -> int:
        State = Enum("State", [
            "STATE_INITIAL",
            "STATE_SIGN",
            "STATE_DIGITS",
            "STATE_END"
        ])

        Chartype = Enum("Chartype", [
            "CHAR_SPACE",
            "CHAR_SIGN",
            "CHAR_NUMBER",
            "CHAR_OTHERS"
        ])

        def toChartype(ch: str) -> Chartype:
            if ch.isdigit():
                return Chartype.CHAR_NUMBER
            elif ch == '+' or ch == '-':
                return Chartype.CHAR_SIGN
            elif ch == " ":
                return Chartype.CHAR_SPACE
            else:
                return Chartype.CHAR_OTHERS

        transfer = {
            State.STATE_INITIAL: {
                Chartype.CHAR_SPACE: State.STATE_INITIAL,
                Chartype.CHAR_SIGN: State.STATE_SIGN,
                Chartype.CHAR_NUMBER: State.STATE_DIGITS,
            },
            State.STATE_SIGN: {
                Chartype.CHAR_NUMBER: State.STATE_DIGITS
            },
            State.STATE_DIGITS: {
                Chartype.CHAR_NUMBER: State.STATE_DIGITS,
                Chartype.CHAR_SPACE: State.STATE_END,
                Chartype.CHAR_SIGN: State.STATE_END,
                Chartype.CHAR_OTHERS: State.STATE_END
            }
        }

        st = State.STATE_INITIAL
        sign = 1
        ans = 0
        for ch in str:
            typ = toChartype(ch)
            if typ not in transfer[st]:
                return 0
            st = transfer[st][typ]
            if st == State.STATE_DIGITS:
                ans *= 10
                ans += int(ch)
            elif st == State.STATE_SIGN:
                sign = -1 if ch == '-' else 1
            elif st == State.STATE_END:
                break
        ans *= sign
        if ans < RANGE[0]:
            return RANGE[0]
        elif ans > RANGE[1]:
            return RANGE[1]
        return ans


class Solution:
    def strToInt(self, str: str) -> int:
        res, i, sign, length = 0, 0, 1, len(str)
        int_max, int_min, bndry = 2 ** 31 - 1, -2 ** 31, 2 ** 31 // 10
        if not str: return 0         # 空字符串，提前返回
        while str[i] == ' ':
            i += 1
            if i == length: return 0 # 字符串全为空格，提前返回
        if str[i] == '-': sign = -1
        if str[i] in '+-': i += 1
        for c in str[i:]:
            if not '0' <= c <= '9' : break
            if res > bndry or res == bndry and c > '7':
                return int_max if sign == 1 else int_min
            res = 10 * res + ord(c) - ord('0')
        return sign * res

# 作者：jyd
# 链接：https://leetcode.cn/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/solution/mian-shi-ti-67-ba-zi-fu-chuan-zhuan-huan-cheng-z-4/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。