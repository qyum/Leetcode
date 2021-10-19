class Solution(object):
    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        # Not possible for even numbers of Nodes
        if n % 2 == 0:
            return []
        
        # Dict (DP) to hold trees 
        dp = collections.defaultdict(list)
        #Build for N == 1
        dp[1] = [TreeNode(0)]
        #Build for N == 3
        temp = TreeNode(0)
        temp.left = TreeNode(0)
        temp.right = TreeNode(0)
        dp[3] = [temp]
        
        # Build for 5,7,.. from previous values
        # Eg. N == 5
        # 1. left sub-tree can have 1 node and right sub-tree can have 3 nodes
        # 2. left sub-tree can have 3 node and right sub-tree can have 1 node
        # For 1. --> create a root node and attach all trees from dp[1] to left and attach all trees from dp[3] to right
        # For 2. --> create a root node and attach all trees from dp[3] to left and attach all trees from dp[1] to left
        
        for i in range(5,n+1,2):
            
            left_possible = 1
            right_possible = (i - 1) - 1 # Deduct 1 for left_possible and 1 root
            
            # This loop increases left_possible by 2 and decreases right by 2
            # So that for N == 7, we attach (dp[1],dp[5]), (dp[3],dp[3]), (dp[5],dp[1]) to root
            while right_possible >= 1:
                
                # These two loops explore all the possibilities for each pair (dp[1],dp[5]), (dp[3],dp[3]), (dp[5],dp[1])
                
                for l_tree in dp[left_possible]:
                    for r_tree in dp[right_possible]:
                        
                        temp = TreeNode(0)
                        temp.left = l_tree
                        temp.right = r_tree
                    
                        dp[i].append(temp)
                left_possible += 2
                right_possible -= 2
        
        return dp[n]
