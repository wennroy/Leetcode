# 寻找下一个排列，维护一个从小到大的数组，最差情况空间复杂度O(n).

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n = str(n)
        sorted_n = n[-1]
        flag = False
        for k in range(len(n)-2,-1,-1):
            tmp = n[k]
            # 寻找大于tmp的值
            if int(tmp) < int(sorted_n[-1]):
                for j, val in enumerate(sorted_n):
                    if int(tmp) < int(val):
                        sorted_n = sorted_n[:j] + tmp + sorted_n[j+1:]
                        first_digit = val
                        flag = True
                        break
            else:
                sorted_n += tmp
            # print(sorted_n)
            if flag:
                ans = n[:k] + first_digit + sorted_n
                BOUNDARY = 2**31
                if int(ans) < -BOUNDARY or int(ans) > BOUNDARY - 1:
                    return -1
                else:
                    return int(ans)
        return -1

# 标答1
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i < 0:
            return -1

        j = len(nums) - 1
        while j >= 0 and nums[i] >= nums[j]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = nums[i + 1:][::-1]
        ans = int(''.join(nums))
        return ans if ans < 2 ** 31 else -1


'''    
标答2: 利用数学方法，我们其实只需要不断比较其最低位数字和次低位数字的大小即可
'''

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        x, cnt = n, 1
        while x >= 10 and x // 10 % 10 >= x % 10:
            cnt += 1
            x //= 10
        x //= 10
        if x == 0:
            return -1

        targetDigit = x % 10
        x2, cnt2 = n, 0
        while x2 % 10 <= targetDigit:
            cnt2 += 1
            x2 //= 10
        x += x2 % 10 - targetDigit  # 把 x2 % 10 换到 targetDigit 上

        MAX_INT = 2 ** 31 - 1
        for i in range(cnt):  # 反转 n 末尾的 cnt 个数字拼到 x 后
            d = n % 10 if i != cnt2 else targetDigit
            # 为了演示算法，请读者把 x 视作一个 32 位有符号整数
            if x > MAX_INT // 10 or x == MAX_INT // 10 and d > 7:
                return -1
            x = x * 10 + d
            n //= 10
        return x
'''
不转换成字符数组，如何用 O(1) 空间复杂度解决此题？

如果还要求不使用 64位整数呢？

类似方法一，我们从 n 开始，不断比较其最低位数字和次低位数字的大小，如果次低位数字不低于最低位数字，则移除最低位数字，继续循环。循环结束后的 n 
就对应着方法一的下标 ii，即 nums 的前 i+1 个字符。

对于方法一中下标 j 的计算也是同理。

最后，我们参考 7. 整数反转的官方题解 的做法，将 i+1 之后的部分反转，即得到下一个整数。如果中途计算会溢出，则返回 −1。


作者：LeetCode-Solution
链接：https://leetcode.cn/problems/next-greater-element-iii/solution/xia-yi-ge-geng-da-yuan-su-iii-by-leetcod-mqf1/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''