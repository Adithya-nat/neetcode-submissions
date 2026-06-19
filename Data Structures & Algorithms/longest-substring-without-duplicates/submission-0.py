class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        best = 0
        seen = {}

        if(len(s) == 1):
            return 1
        
        for right, ch in enumerate(s):
            if ch in seen and seen[ch] >= left:
                left = seen[ch] + 1
            
            seen[s[right]] = right
            best = max(best, right-left + 1)
        
        return best


            

            

            

            
            


        
        