class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        x = max(a, b, c)
        y = min(a, b, c)
        z = a + b + c - x - y
        # if sum of two small less then max
        # pair each set with max has maximum solution
        if y + z <= x:
            return y + z

        # otherwise, keep difference of two small set <=1
        # after take away max we can calculate the reat gives
        # floor (a+b+c)/2
        else:
            return (a + b + c) // 2