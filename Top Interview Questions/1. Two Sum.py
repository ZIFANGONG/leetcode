class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        num_to_idx = {}

        for i in range(len(nums)):
            
            need = target - nums[i]

            if need in num_to_idx:
                return [num_to_idx[need], i]

            num_to_idx[nums[i]] = i
        