# 各种判断已经遍历区间需要注意。
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        ans = []
        for first in range(n-2):
            if first == 0 or nums[first-1] != nums[first]:
                third = n - 1
                for second in range(first+1, n-1):
                    if second > first + 1 and nums[second] == nums[second - 1]:
                        continue

                    while third > second + 1 and nums[first] + nums[second] + nums[third] > 0:
                        third -= 1

                    if second == third:
                        break

                    if nums[first] + nums[second] + nums[third] == 0:
                        # print(first, second, third)
                        ans.append([nums[first], nums[second], nums[third]])
        return ans

# 标答
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()

        # 枚举 a
        for first in range(n):
            # 需要和上一次枚举的数不相同
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # c 对应的指针初始指向数组的最右端
            third = n - 1
            target = -nums[first]
            # 枚举 b
            for second in range(first + 1, n):
                # 需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证 b 的指针在 c 的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans

'''
作者：LeetCode - Solution
链接：https: // leetcode.cn / problems / 3
sum / solution / san - shu - zhi - he - by - leetcode - solution /
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        if (not nums or n < 3):
            return []
        nums.sort()
        res = []
        for i in range(n):
            if (nums[i] > 0):
                return res
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            L = i + 1
            R = n - 1
            while (L < R):
                if (nums[i] + nums[L] + nums[R] == 0):
                    res.append([nums[i], nums[L], nums[R]])
                    while (L < R and nums[L] == nums[L + 1]):
                        L = L + 1
                    while (L < R and nums[R] == nums[R - 1]):
                        R = R - 1
                    L = L + 1
                    R = R - 1
                elif (nums[i] + nums[L] + nums[R] > 0):
                    R = R - 1
                else:
                    L = L + 1
        return res

'''
排序 + 双指针
本题的难点在于如何去除重复解。

算法流程：
特判，对于数组长度 n，如果数组为 null 或者数组长度小于 3，返回 []。
对数组进行排序。
遍历排序后数组：
若 nums[i]>0nums[i]>0：因为已经排序好，所以后面不可能有三个数加和等于 0，直接返回结果。
对于重复元素：跳过，避免出现重复解
令左指针 L=i+1，右指针 R=n-1，当 L<R 时，执行循环：
当 nums[i]+nums[L]+nums[R]==0，执行循环，判断左界和右界是否和下一位置重复，去除重复解。并同时将 L,R 移到下一位置，寻找新的解
若和大于 0，说明 nums[R] 太大，R 左移
若和小于 0，说明 nums[L] 太小，L 右移
复杂度分析
时间复杂度：O\left(n^{2}\right)O(n 2)，数组排序 O(N \log N)O(NlogN)，遍历数组 O\left(n\right)O(n)，双指针遍历 O\left(n\right)O(n)，总体 O(N \log N)+O\left(n\right)*O\left(n\right)O(NlogN)+O(n)∗O(n)，O\left(n^{2}\right)O(n 2)
空间复杂度：O(1)O(1)

作者：wu_yan_zu
链接：https: // leetcode.cn / problems / 3
sum / solution / pai - xu - shuang - zhi - zhen - zhu - xing - jie - shi - python3 - by /
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
