#sliding window solution

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        start, end= 0, 0
        n, freq_map = len(s), defaultdict(int)
        most_repeating_char, answer = 0, 0
        
        for end in range(n):
            c = s[end]
            freq_map[c] += 1
            print(freq_map[c])
            
            # Most repeating char, which contributes to our answer
            most_repeating_char = max(most_repeating_char, freq_map[c]) 
            
            # If the window has more than k chars other than most repeating one.
            if end-start+1 - most_repeating_char > k:  
                freq_map[s[start]] -= 1
                start += 1
            
            answer = max(answer, end-start+1)
    
        return answer
