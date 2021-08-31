#bfs reucursive solution

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        
        def dfs(arr):
            if arr:
                m=max(arr)
                ind=arr.index(m)
                return TreeNode(m,dfs(arr[:ind]),dfs(arr[ind+1:]))
        return dfs(nums)
