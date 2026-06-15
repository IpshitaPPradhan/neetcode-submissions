class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char = dict(Counter(s))
        t_char = dict(Counter(t))
        if s_char == t_char:
           return True
        return False
        