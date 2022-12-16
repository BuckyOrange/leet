class Solution:
    def maxArea(self, height: List[int]) -> int:
        #double pointer,
        #move shorter one will possiblly increase, move longer one will decrease for sure.
        #so we move shorter one every time.
        i, j, res  =  0, len(height)-1, 0
        while i < j:
            if height[i] > height[j]:
                res = max(res, height[j]*(j-i))
                j -= 1
            else:
                res = max(res, height[i]*(j-i))
                i += 1
        return res