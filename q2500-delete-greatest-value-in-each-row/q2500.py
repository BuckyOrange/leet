class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        # sort and transpose. sum max element of each row to get answer
        for i in grid:
            i.sort()
        tmp = 0

        for i in list(zip(*grid)):
            tmp += max(i)

        return tmp