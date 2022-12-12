class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s

        res = ['' for _ in range(numRows)]
        c, flag = 0, -1
        for i in s:
            res[c] += i
            if c == 0 or c == numRows - 1:
                flag = -flag
            c += flag
        return ''.join(res)

        # initialize n row residual, then add each character to row one at a time.
        # when reach 0 or numRows, change direction.
