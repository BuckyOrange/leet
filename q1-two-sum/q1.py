def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    #simply use dic to search two number
    dic = {}
    for i in range(len(nums)):
        if (target - nums[i]) in dic:
            return [dic[target - nums[i]], i]
        else:
            dic[nums[i]] = i