"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

四叉树兄弟题在 558. 建立四叉树
"""


class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf and quadTree2.isLeaf:
            return Node(quadTree1.val | quadTree2.val, 1, None, None, None, None)
        elif not quadTree1.isLeaf and not quadTree2.isLeaf:
            cur_pt = Node(1, 0, self.intersect(quadTree1.topLeft, quadTree2.topLeft),
                          self.intersect(quadTree1.topRight, quadTree2.topRight),
                          self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft),
                          self.intersect(quadTree1.bottomRight, quadTree2.bottomRight))
            if cur_pt.topLeft.isLeaf and cur_pt.topRight.isLeaf and cur_pt.bottomRight.isLeaf and cur_pt.bottomLeft.isLeaf and cur_pt.topLeft.val == cur_pt.topRight.val == cur_pt.bottomRight.val == cur_pt.bottomLeft.val:
                return Node(cur_pt.topLeft.val, 1, None, None, None, None)
            else:
                return cur_pt
        elif quadTree1.isLeaf:
            isLeaf_pt = quadTree1
            notLeaf_pt = quadTree2
        else:
            isLeaf_pt = quadTree2
            notLeaf_pt = quadTree1

        cur_pt = Node(1, 0, self.intersect(Node(isLeaf_pt.val, 1, None, None, None, None), notLeaf_pt.topLeft),
                      self.intersect(Node(isLeaf_pt.val, 1, None, None, None, None), notLeaf_pt.topRight),
                      self.intersect(Node(isLeaf_pt.val, 1, None, None, None, None), notLeaf_pt.bottomLeft),
                      self.intersect(Node(isLeaf_pt.val, 1, None, None, None, None), notLeaf_pt.bottomRight))

        if cur_pt.topLeft.isLeaf and cur_pt.topRight.isLeaf and cur_pt.bottomRight.isLeaf and cur_pt.bottomLeft.isLeaf and cur_pt.topLeft.val == cur_pt.topRight.val == cur_pt.bottomRight.val == cur_pt.bottomLeft.val:
            return Node(cur_pt.topLeft.val, 1, None, None, None, None)
        else:
            return cur_pt


'''
终于过了，这四叉树debug真的折磨人
前前后后搞了一个小时

最后的问题：当一棵树
[val, isLeaf]

[1,0]
[1,1] [1,0] [1,1] [1,1]
        |
    []......[]
的时候，我们仍然需要判断isLeaf是否为1，而不能轻易总结数值一样的结点可以被归总为[1,1]

执行用时：72 ms, 在所有 Python3 提交中击败了47.14%的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了62.86%的用户
'''

'''
标答：我们在考虑问题时应当考虑较为特殊的情况，包括但不限于当val值为1时，无论怎么另一棵树怎么操作，值一定是1

'''

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf:
            return Node(True, True) if quadTree1.val else quadTree2
        if quadTree2.isLeaf:
            return self.intersect(quadTree2, quadTree1)
        o1 = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        o2 = self.intersect(quadTree1.topRight, quadTree2.topRight)
        o3 = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        o4 = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
        if o1.isLeaf and o2.isLeaf and o3.isLeaf and o4.isLeaf and o1.val == o2.val == o3.val == o4.val:
            return Node(o1.val, True)
        return Node(False, False, o1, o2, o3, o4)

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/solution/si-cha-shu-jiao-ji-by-leetcode-solution-wy1u/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。