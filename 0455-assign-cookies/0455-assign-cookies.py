class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        gn=len(g)
        sn=len(s)
        i,j=0,0
        while i<gn and j<sn:
            if s[j]>=g[i]:
                i+=1
            j+=1
        return i