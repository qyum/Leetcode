class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        stack = [0]
        for i in s:
            if i == '(':
                stack.append(0)
            else:
                x = stack.pop()
                #print(x)
                stack[-1] += max(2*x,1)
                print(stack[-1])
                
        return stack[0]
