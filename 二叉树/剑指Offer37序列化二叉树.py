# 用DICT来实现序列化 + DFS

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import json


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "{}"
        str_dict = {}

        def dfs(root, pt):
            pt[root.val] = {}
            pt = pt[root.val]
            if root.left:
                pt["l"] = {}
                dfs(root.left, pt['l'])
            if root.right:
                pt["r"] = {}
                dfs(root.right, pt['r'])

        dfs(root, str_dict)
        return json.dumps(str_dict)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        tree_dict = json.loads(data)
        if not tree_dict:
            return None
        for val in tree_dict.keys():
            head = TreeNode(val)
        pt = tree_dict[val]

        def dfs(pt, root):
            if 'l' in pt.keys():
                for val in pt['l'].keys():
                    root.left = TreeNode(int(val))
                    dfs(pt['l'][val], root.left)
            if 'r' in pt.keys():
                for val in pt['r'].keys():
                    root.right = TreeNode(int(val))
                    dfs(pt['r'][val], root.right)

        dfs(pt, head)
        return head

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


class Codec:
    def serialize(self, root):
        if not root: return "[]"
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else: res.append("null")
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        if data == "[]": return
        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root

# 作者：jyd
# 链接：https://leetcode.cn/problems/xu-lie-hua-er-cha-shu-lcof/solution/mian-shi-ti-37-xu-lie-hua-er-cha-shu-ceng-xu-bian-/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。