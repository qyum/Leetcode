class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in range(len(s)):
            if s[i]!=')':
                stack.append(s[i])
            else:
                stri = ''
                while stack and stack[-1]!='(':
                    stri += stack.pop()
                stack.pop()
                for st in stri:
                    stack.append(st)
        return ''.join(stack)
      
