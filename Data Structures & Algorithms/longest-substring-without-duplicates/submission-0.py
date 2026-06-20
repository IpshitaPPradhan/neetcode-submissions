class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        l = 0
        r = 0
        max_length = 0

        
        while r < len(s):
            if s[r] not in unique:
                unique.add(s[r])
                r += 1
                max_length = max(max_length, r - l)
                
                
            elif s[r] in unique:
                unique.remove(s[l])
                l += 1
        return max_length

        
        