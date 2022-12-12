class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #pop if we meet any duplicate
        prev = ''
        i = 0
        while i < len(nums):
            if nums[i] == prev:
                nums.pop(i)
            else:
                prev = nums[i]
                i += 1
        return i

    def removeDuplicates(self, nums: List[int]) -> int:
        #exchange all distinct element ahead
        i = 0
        for x in nums:
            if i == 0 or nums[i - 1] != x:
                nums[i] = x
                i += 1
        return i