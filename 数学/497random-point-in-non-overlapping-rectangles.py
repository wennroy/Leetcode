import math
import random

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rect_volume = []
        self.rects = rects
        self.rect_volume_sum = 0
        for rect in rects:
            delta_x = math.floor(rect[2]) - math.ceil(rect[0]) + 1
            delta_y = math.floor(rect[3]) - math.ceil(rect[1]) + 1
            self.rect_volume_sum += delta_x*delta_y
            self.rect_volume.append(self.rect_volume_sum)

    def pick(self) -> List[int]:
        rand = random.random() * self.rect_volume_sum
        for i, cdf_volume in enumerate(self.rect_volume):
            if rand <= cdf_volume:
                break
        rect = self.rects[i]
        delta_x = math.floor(rect[2]) - math.ceil(rect[0]) + 1
        delta_y = math.floor(rect[3]) - math.ceil(rect[1]) + 1
        rand_int = random.randint(0, delta_x*delta_y-1)
        x = math.ceil(rect[0]) + int(rand_int / delta_y)
        y = math.ceil(rect[1]) + rand_int % delta_y
        return [x,y]

import bisect

class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.sum = [0]
        for a, b, x, y in rects:
            self.sum.append(self.sum[-1] + (x - a + 1) * (y - b + 1))

    def pick(self) -> List[int]:
        k = random.randrange(self.sum[-1])
        rectIndex = bisect.bisect_right(self.sum, k) - 1
        a, b, _, y = self.rects[rectIndex]
        da, db = divmod(k - self.sum[rectIndex], y - b + 1)
        return [a + da, b + db]
'''
前缀和 + 二分查找
有提到矩形输入必为整数，忽视了。 Solution(int[][] rects) 用给定的矩形数组 rects 初始化对象。
random.randrange(x) 函数更方便生成int
bisect.bisect_right(a,k) 二分查找，寻找抽到的矩阵 (a中第一个大于k的元素)

bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None):  
The returned insertion point i partitions the array a into two halves so that 
all(val < x for val in a[lo : i]) for the left side and 
all(val >= x for val in a[i : hi]) for the right side.
a = [1,5,6,7,8,9]
bisect.bisect_right(a,8)
Out[42]: 5
bisect.bisect_left(a,8)
Out[43]: 4

divmod(8,3) = (2,2)

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/random-point-in-non-overlapping-rectangles/solution/fei-zhong-die-ju-xing-zhong-de-sui-ji-di-6s33/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''