class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        Stack = []
        
        
        for i in ops:
            if (i == 'C'):
                Stack.pop()
                
            elif (i == 'D'):
                Stack.append(2*int(Stack[-1]))
                
            elif (i == '+'):
                Stack.append(int(Stack[-1]) + int(Stack[-2]))
            
            else:
                Stack.append(int(i))

            
        return sum(Stack)
