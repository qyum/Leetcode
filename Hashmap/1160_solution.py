from collections import Counter

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        sum=0
        char_count=Counter(chars)
        #print(char_count)
        for w in words:
            print(Counter(w))
            print(char_count==Counter(w))
            if Counter(w)&char_count==Counter(w):
                #print(w)
                sum+=len(w)
        #print(sum)
        
        return sum
