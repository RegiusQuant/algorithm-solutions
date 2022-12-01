from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.prev = TreeNode(float("-inf"))
        self.node1, self.node2 = None, None

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.traverse(root)
        self.node1.val, self.node2.val = self.node2.val, self.node1.val

    def traverse(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        self.traverse(root.left)

        if self.node1 is None and self.prev.val >= root.val:
            self.node1 = self.prev
        if self.node1 and self.prev.val >= root.val:
            self.node2 = root
        self.prev = root

        self.traverse(root.right)
