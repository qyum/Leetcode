class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(left, right):
            
            if left <= right:
                mid = left + (right - left) // 2 # or (@left + @right) // 2
                return TreeNode(nums[mid],
                               helper(left, mid - 1),
                               helper(mid + 1, right))
            return None         # TODO: is this necessary?
        
        return helper(0, len(nums) - 1)
