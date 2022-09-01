INT_MAX = 2147483648


class Solution:
    def divide(self, a: int, b: int) -> int:
        sign = 1
        if a > 0 and b < 0:
            b = -b
            sign = -1
        elif a < 0 and b > 0:
            a = -a
            sign = -1
        elif a < 0 and b < 0:
            a, b = -a, -b

        res_b = []
        new_b = b
        count = []
        cur_count = 1
        while new_b <= a:
            res_b.append(new_b)
            count.append(cur_count)
            cur_count += cur_count
            new_b += new_b
        # print(count, res_b)
        n = len(res_b)
        ans = 0
        for i in range(n - 1, -1, -1):
            if a - res_b[i] >= 0:
                a -= res_b[i]
                ans += count[i]
            if a == 0:
                break

        ans *= sign
        if ans >= INT_MAX - 1:
            return INT_MAX - 1
        elif ans <= -INT_MAX:
            return -INT_MAX

        return ans


# 二分查找
class Solution:
    def divide(self, a: int, b: int) -> int:
        INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

        # 考虑被除数为最小值的情况
        if a == INT_MIN:
            if b == 1:
                return INT_MIN
            if b == -1:
                return INT_MAX

        # 考虑除数为最小值的情况
        if b == INT_MIN:
            return 1 if a == INT_MIN else 0
        # 考虑被除数为 0 的情况
        if a == 0:
            return 0

        # 一般情况，使用二分查找
        # 将所有的正数取相反数，这样就只需要考虑一种情况
        rev = False
        if a > 0:
            a = -a
            rev = not rev
        if b > 0:
            b = -b
            rev = not rev

        # 快速乘
        def quickAdd(y: int, z: int, x: int) -> bool:
            # x 和 y 是负数，z 是正数
            # 需要判断 z * y >= x 是否成立
            result, add = 0, y
            while z > 0:
                if (z & 1) == 1:
                    # 需要保证 result + add >= x
                    if result < x - add:
                        return False
                    result += add
                if z != 1:
                    # 需要保证 add + add >= x
                    if add < x - add:
                        return False
                    add += add
                # 不能使用除法
                z >>= 1
            return True

        left, right, ans = 1, INT_MAX, 0
        while left <= right:
            # 注意溢出，并且不能使用除法
            mid = left + ((right - left) >> 1)
            check = quickAdd(b, mid, a)
            if check:
                ans = mid
                # 注意溢出
                if mid == INT_MAX:
                    break
                left = mid + 1
            else:
                right = mid - 1

        return -ans if rev else ans


# 作者：LeetCode - Solution
# 链接：https: // leetcode.cn / problems / xoh6Oh / solution / zheng - shu - chu - fa - by - leetcode - solution - 3572 /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。