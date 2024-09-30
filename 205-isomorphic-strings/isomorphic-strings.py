class Solution:
    def isIsomorphic(self, s: str, t: str):
        l=[]
        l1=[]
        for i in s:
            l.append(s.index(i))
        for i in t:
            l1.append(t.index(i))
        if l==l1:
            return True
        return False