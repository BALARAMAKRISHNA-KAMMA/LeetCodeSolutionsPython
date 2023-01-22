class Solution:
    def romanToInt(self, s: str) -> int:
        dictr={'I':1,'V':5,'X':10,'M':1000,'C':100,'D':500,'L':50}
        le=len(s)
        num=dictr[s[le-1]]
        for i in range(le-2,-1,-1):
            if dictr[s[i]]>=dictr[s[i+1]]:
                num+=dictr[s[i]]
            else:
                num-=dictr[s[i]]
        return num
