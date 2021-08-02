#Time complexity o(n)
#space complexity o(n)
#stack solution

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0 for te in range(len(temperatures))]
        
        for i, t1 in enumerate(temperatures):
            #print(stack[-1][1])
            #print(t1)
            #print(stack)
            while stack and t1 > stack[-1][1]:
                #print(stack[-1][1])
                j, t2 = stack.pop()
                #print(i,j)
                res[j] = i - j
            stack.append((i, t1))
        #print(stack)
        return res
