class Solution:
    def reverse(self, x: int) -> int:
        
        if x > 0:
            res = int(str(x)[::-1])
        else:
            res = int(str(x * -1)[::-1]) * -1

        mi = 2 ** 31 * (-1)
        ma = 2 ** 31 - 1

        if res < mi or res > ma: return 0
        return res
