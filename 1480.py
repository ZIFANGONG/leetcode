class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        sum = 0
        for i in nums:
            sum += i
            result.append(sum)
        return result