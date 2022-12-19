class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #single pointer way
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        for i in range(ptr, len(nums)):
            if nums[i] == 1:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        return nums


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #double pointer way
        ptr0, ptr1 = 0, 0

        for i in range(len(nums)):
            if nums[i] == 1:
                nums[i], nums[ptr1] = nums[ptr1], nums[i]
                ptr1 += 1
            elif nums[i] == 0:
                nums[i], nums[ptr0] = nums[ptr0], nums[i]
                if ptr0 < ptr1:
                    nums[i], nums[ptr1] = nums[ptr1], nums[i]
                ptr0 += 1
                ptr1 += 1

        return nums