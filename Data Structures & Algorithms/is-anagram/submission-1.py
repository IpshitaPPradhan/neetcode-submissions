class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
           return False
        return dict(Counter(s)) == dict(Counter(t))
        