class Solution:
    def isPalindrome(self, x: int) -> bool:
        org=x
        if x<0:
            return False
        if x!=0 and x%10==0:
            return False
        res=0
        while(x!=0):
            rem=x%10
            res=res * 10 + rem
            x =x // 10
        return True if res==org else False
