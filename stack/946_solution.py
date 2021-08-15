class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack=[]
        curr=0
        
        for i in range(len(pushed)):
            stack.append(pushed[i])
            print(stack)
            
            while stack and stack[-1]==popped[curr]:
                stack.pop()
                curr+=1
        

        return not stack
