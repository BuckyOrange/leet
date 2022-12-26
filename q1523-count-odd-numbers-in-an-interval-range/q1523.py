class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return high - low + 1 - (high // 2 - (low - 1) // 2)



