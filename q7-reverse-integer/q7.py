class Solution:
    def reverse(self, x: int) -> int:
        if x > 2**31 or x < -2**31:
            return 0
        a = x < 0
        b = int(str(abs(x))[::-1])
        if b > 2**31 or b < -2**31:
            return 0
        elif a:
            return -b
        return b