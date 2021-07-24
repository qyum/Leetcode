class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def minute(a):
            #print(a[:2],a[-2:])
            #print(int(a[:2]) * 60 + int(a[-2:]))
            return int(a[:2]) * 60 + int(a[-2:])
        
        x=timePoints.sort()
        print(x)
        ans = 24*60   #on basis of day or half day
        for i in range(len(timePoints)):
            j = (i + 1) % len(timePoints)
            #print(j,i)
            #print(timePoints[j],timePoints[i])
            #print(minute(timePoints[j]),minute(timePoints[i]))
            ans = min(ans, (minute(timePoints[j]) - minute(timePoints[i])) % 1440)
        return ans  
