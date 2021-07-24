class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        
        left = 0
        d = {}
        max_length = 0
        curr_index = 0
        
        
        while curr_index <len(fruits):
            if len(d)<=2:
                if fruits[curr_index] not in d:
                    d[fruits[curr_index]] = 1
                else:
                    d[fruits[curr_index]] += 1
                    print(d[fruits[curr_index]])

            while len(d)>2:
                print(d[fruits[left]])
                
                d[fruits[left]] -= 1
                if d[fruits[left]] == 0:
                    d.pop(fruits[left])
                left += 1
                
            print(max_length,curr_index,left)    
            max_length = max(max_length,curr_index+1-left)
            curr_index += 1

        return max_length
