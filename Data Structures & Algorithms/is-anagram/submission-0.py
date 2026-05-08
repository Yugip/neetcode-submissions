class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = list(s)
        tlist = list(t)
        if sorted(tlist) == sorted(slist):
            return True
        else:
            return False