class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        tmp = -2**31
        for i in strs:
            if not i.isnumeric():
                tmp = max(tmp, len(i))
            else:
                tmp = max(tmp, int(i))
        return tmp

class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        #very thoughful way to use try expect.
        ans = 0
        for s in strs:
            try: x = int(s)
            except: x = len(s)
            ans = max(ans, x)
        return ans

