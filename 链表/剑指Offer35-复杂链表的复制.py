"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        copyHead = Node(head.val)
        copy_pt = copyHead
        pt = head
        stack1 = [head]
        stack2 = [copyHead]
        while pt.next:
            pt = pt.next
            copy_pt.next = Node(pt.val)
            copy_pt = copy_pt.next
            stack1.append(pt)
            stack2.append(copy_pt)

        pt = head
        i = 0
        n = len(stack1)
        while pt:
            if pt.random:
                for j in range(n):
                    if stack1[j] == pt.random:
                        break
                stack2[i].random = stack2[j]
            pt = pt.next
            i += 1
        return copyHead

# Python deepcopy yyds
import copy

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        p=copy.deepcopy(head)
        return p