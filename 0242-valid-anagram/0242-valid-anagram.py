class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(t) == sorted(s) and len(t) == len(s)
