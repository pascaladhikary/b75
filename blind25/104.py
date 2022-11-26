class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
                return 0

        l, r = self.maxDepth(root.left), self.maxDepth(root.right)
        return 1 + max(l, r)