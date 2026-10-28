class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=list(s)
        a1=sorted(a)
        b=list(t)
        b1=sorted(b)
        r1=''.join(a1)
        r2=''.join(b1)
        if r1==r2:
            return True
        else:
            return False