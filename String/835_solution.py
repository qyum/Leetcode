class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        
        
        a_1 = []
        b_1 = []
        for i in range(len(img1)):
            for j in range(len(img1[0])):
                #print("ith",img1[i][j])
                if img1[i][j] == 1:
                    a_1.append((i,j))
                if img2[i][j] == 1:
                    b_1.append((i,j))
        print( a_1,b_1)
        
        d = {}
        ans = 0
        for a_x, a_y in a_1:
            for b_x,b_y in  b_1:
                tr = (b_x - a_x, b_y - a_y)
                #print("tr",tr)
                if tr in d:
                    d[tr] += 1
                else:
                    d[tr] = 1
                #print(d[tr])
                ans = max(ans, d[tr])
        #print(d)
        return ans
