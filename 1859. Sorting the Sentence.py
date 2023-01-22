class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(" ")
        l = [0] * len(s)
        for i in range(len(s)):
            ind = int(s[i][-1])
            l[ind-1] = s[i][:-1:]
        return ' '.join(l)
