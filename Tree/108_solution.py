class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # base case
        if not nums: 
            return None
        
        # getting the mid
        mid = len(nums)//2
        node = TreeNode(nums[mid])
        
        # left node is given the responsibility till mid, 
        # but not including mid
        node.left = self.sortedArrayToBST(nums[:mid])
        # right node is given the responsibility from mid+1 
        # till the end
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node
