#475. Heaters
#problem_link:https://leetcode.com/problems/heaters/

#........o(nlogn) time complexity+o(1)space complexity solution.................................

def binary_search(house, heaters):
    left = 0
    right = len(heaters)-1
    
    while left <= right:
        mid = (left+right)//2
    
        if house < heaters[mid]:
            right = mid - 1
        elif house > heaters[mid]:
            left = mid + 1
        else:
            return 0
        
    print(right,left)
        
    if right < 0:
        return heaters[left]-house
    elif left > len(heaters)-1:
        return house-heaters[right]
    else:  
        return min(heaters[left]-house, house-heaters[right])

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        
        
        heaters.sort() #O(nlogn)
        
        radius = 0
        for h in houses:
            distance =binary_search(h, heaters)
            #print(distance)
            radius = max(radius, distance)
        return radius
