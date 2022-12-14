class Solution:
    def myAtoi(self, s: str) -> int:
        #regular expression
        return min(max(int(*re.findall('^[\+\-]?\d+', s.lstrip())), -2**31), 2**31-1)