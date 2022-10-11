# 二叉树的反序列化：前序遍历+中序遍历 => 决定一棵二叉树
# 再利用额外的O(n)空间存储结点对应的值
# 总共时间复杂度O(n)，空间复杂度O(3*n)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # 通过中序遍历和前序遍历来返回一棵完整的二叉树
        ans_in = []
        ans_pre = []
        node_val = []
        count = -1

        def in_pre_order(root):
            nonlocal ans_in, ans_pre, count
            if not root:
                return
            count += 1
            val = count
            node_val.append(str(root.val))
            ans_pre.append(str(val))
            in_pre_order(root.left)
            ans_in.append(str(val))
            in_pre_order(root.right)
            return

        in_pre_order(root)
        # print(ans_in, ans_pre)
        return ','.join(ans_pre) + ' ' + ','.join(ans_in) + ' ' + ','.join(node_val)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        pre_list, in_list, node_val = data.split(' ')
        if not in_list:
            return None
        pre_list = list(map(int, pre_list.split(',')))
        in_list = list(map(int, in_list.split(',')))
        node_val = list(map(int, node_val.split(',')))

        def recur(in_list, pre_list):
            if not in_list:
                return None
            root = TreeNode(node_val[pre_list[0]])
            for i, val in enumerate(in_list):
                if val == pre_list[0]:
                    idx = i
                    break
            root.left = recur(in_list[:idx], pre_list[1:idx + 1])
            root.right = recur(in_list[idx + 1:], pre_list[idx + 1:])

            return root

        root = recur(in_list, pre_list)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# DFS

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List
class Codec:

    def serialize(self, root):
        if not root:
            return "null,"
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return str(root.val) + ',' + left + right

    def dfs(self, res: List) -> TreeNode:
        val = res.pop(0)
        if val == 'null':
            return None
        root = TreeNode(val)
        root.left = self.dfs(res)
        root.right = self.dfs(res)
        return root

    def deserialize(self, data):
        root = self.dfs(data.split(','))
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# 作者：san - er - yi - 4
# 链接：https: // leetcode.cn / problems / serialize - and -deserialize - binary - tree / solution / by - san - er - yi - 4 - 0
# nes /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。