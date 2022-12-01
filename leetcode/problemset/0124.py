from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.result = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.traverse(root)
        return self.result

    def traverse(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftMaxSum = max(0, self.traverse(root.left))
        rightMaxSum = max(0, self.traverse(root.right))
        self.result = max(self.result, leftMaxSum + rightMaxSum + root.val)

        return max(leftMaxSum, rightMaxSum) + root.val
