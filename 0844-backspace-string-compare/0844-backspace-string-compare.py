class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1=[]
        stack2=[]
        nS=len(s)
        nT=len(t)
        for i in range(nS):
            if s[i]!="#":
                stack1.append(s[i])
            elif stack1:
                stack1.pop()
        for i in range(nT):
            if t[i]!="#":
                stack2.append(t[i])
            elif stack2:
                stack2.pop()
        if stack1==stack2:
            return True
        else: 
            return False