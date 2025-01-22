class Solution(object):
    def twoSum(self, nums, target):

        pair_index={}

        for i, num in enumerate(nums):
            if target - num in pair_index:
                return [pair_index[target - num], i]
            pair_index[num] = i
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """