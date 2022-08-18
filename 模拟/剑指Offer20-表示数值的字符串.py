# 用ifelse构成的有限状态自动机
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        state = ['begin', '+/-1', 'digit1', 'dot1', 'dot2', 'digit2',
                 'E/e', '+/-2', 'digit3']
        cs = 'begin'
        for l in s:
            if cs == 'begin':
                if l == '+' or l == '-':
                    cs = '+/-1'
                elif l.isdigit():
                    cs = 'digit1'
                elif l == '.':
                    cs = 'dot2'
                else:
                    return False

            elif cs == '+/-1':
                if l.isdigit():
                    cs = 'digit1'
                elif l == '.':
                    cs = 'dot2'
                else:
                    return False

            elif cs == 'digit1':
                if l.isdigit():
                    continue
                elif l == '.':
                    cs = 'dot1'
                elif l == 'E' or l == 'e':
                    cs = 'E/e'
                else:
                    return False

            elif cs == 'dot1':
                if l.isdigit():
                    cs = 'digit2'
                elif l == 'E' or l == 'e':
                    cs = 'E/e'
                else:
                    return False

            elif cs == 'dot2':
                if l.isdigit():
                    cs = 'digit2'
                else:
                    return False

            elif cs == 'digit2':
                if l.isdigit():
                    continue
                elif l == 'E' or l == 'e':
                    cs = 'E/e'
                else:
                    return False

            elif cs == 'E/e':
                if l.isdigit():
                    cs = 'digit3'
                elif l == '+' or l == '-':
                    cs = '+/-2'
                else:
                    return False

            elif cs == '+/-2':
                if l.isdigit():
                    cs = 'digit3'
                else:
                    return False

            else:
                if not l.isdigit():
                    return False

        return True and (cs[:5] == 'digit' or cs[:4] == 'dot1')


# 标答的自动机，好酷啊
# 我怎么就想不到这种方法呢

from enum import Enum
class Solution:
    def isNumber(self, s: str) -> bool:
        State = Enum("State", [
            "STATE_INITIAL",
            "STATE_INT_SIGN",
            "STATE_INTEGER",
            "STATE_POINT",
            "STATE_POINT_WITHOUT_INT",
            "STATE_FRACTION",
            "STATE_EXP",
            "STATE_EXP_SIGN",
            "STATE_EXP_NUMBER",
            "STATE_END"
        ])
        Chartype = Enum("Chartype", [
            "CHAR_NUMBER",
            "CHAR_EXP",
            "CHAR_POINT",
            "CHAR_SIGN",
            "CHAR_SPACE",
            "CHAR_ILLEGAL"
        ])

        def toChartype(ch: str) -> Chartype:
            if ch.isdigit():
                return Chartype.CHAR_NUMBER
            elif ch.lower() == "e":
                return Chartype.CHAR_EXP
            elif ch == ".":
                return Chartype.CHAR_POINT
            elif ch == "+" or ch == "-":
                return Chartype.CHAR_SIGN
            elif ch == " ":
                return Chartype.CHAR_SPACE
            else:
                return Chartype.CHAR_ILLEGAL

        transfer = {
            State.STATE_INITIAL: {
                Chartype.CHAR_SPACE: State.STATE_INITIAL,
                Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                Chartype.CHAR_POINT: State.STATE_POINT_WITHOUT_INT,
                Chartype.CHAR_SIGN: State.STATE_INT_SIGN
            },
            State.STATE_INT_SIGN: {
                Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                Chartype.CHAR_POINT: State.STATE_POINT_WITHOUT_INT
            },
            State.STATE_INTEGER: {
                Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                Chartype.CHAR_EXP: State.STATE_EXP,
                Chartype.CHAR_POINT: State.STATE_POINT,
                Chartype.CHAR_SPACE: State.STATE_END
            },
            State.STATE_POINT: {
                Chartype.CHAR_NUMBER: State.STATE_FRACTION,
                Chartype.CHAR_EXP: State.STATE_EXP,
                Chartype.CHAR_SPACE: State.STATE_END
            },
            State.STATE_POINT_WITHOUT_INT: {
                Chartype.CHAR_NUMBER: State.STATE_FRACTION
            },
            State.STATE_FRACTION: {
                Chartype.CHAR_NUMBER: State.STATE_FRACTION,
                Chartype.CHAR_EXP: State.STATE_EXP,
                Chartype.CHAR_SPACE: State.STATE_END
            },
            State.STATE_EXP: {
                Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER,
                Chartype.CHAR_SIGN: State.STATE_EXP_SIGN
            },
            State.STATE_EXP_SIGN: {
                Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER
            },
            State.STATE_EXP_NUMBER: {
                Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER,
                Chartype.CHAR_SPACE: State.STATE_END
            },
            State.STATE_END: {
                Chartype.CHAR_SPACE: State.STATE_END
            },
        }

        st = State.STATE_INITIAL
        for ch in s:
            typ = toChartype(ch)
            if typ not in transfer[st]:
                return False
            st = transfer[st][typ]

        return st in [State.STATE_INTEGER, State.STATE_POINT, State.STATE_FRACTION, State.STATE_EXP_NUMBER,
                      State.STATE_END]


# 作者：LeetCode - Solution
# 链接：https://leetcode.cn/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/solution/biao-shi-shu-zhi-de-zi-fu-chuan-by-leetcode-soluti/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。