class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if firstList==[] and secondList==[]:
            return []
        
        
        out = []
        i, j = 0, 0
        
        # Traverse
        while i < len(firstList) and j < len(secondList):
            # Overlap
            if secondList[j][1] >= firstList[i][0]:
                start = max(firstList[i][0], secondList[j][0])
                end = min(firstList[i][1], secondList[j][1])
                # Otherwise implies no overlap
                if start <= end:
                    out.append([start, end])
            # Update pointers
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return out
