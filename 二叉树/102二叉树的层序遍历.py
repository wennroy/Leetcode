# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        nxtLevel = [root]
        ans = []
        ans.append([root.val])
        while nxtLevel:
            curLevel = nxtLevel
            nxtLevel = []
            tmp_list = []
            for node in curLevel:
                if node.left:
                    nxtLevel.append(node.left)
                    tmp_list.append(node.left.val)
                if node.right:
                    nxtLevel.append(node.right)
                    tmp_list.append(node.right.val)

            ans.append(tmp_list)
        ans.pop()
        return ans

# BFS

'''
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector <vector <int>> ret;
        if (!root) {
            return ret;
        }

        queue <TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            int currentLevelSize = q.size();
            ret.push_back(vector <int> ());
            for (int i = 1; i <= currentLevelSize; ++i) {
                auto node = q.front(); q.pop();
                ret.back().push_back(node->val);
                if (node->left) q.push(node->left);
                if (node->right) q.push(node->right);
            }
        }
        
        return ret;
    }
};

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/binary-tree-level-order-traversal/solution/er-cha-shu-de-ceng-xu-bian-li-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

'''