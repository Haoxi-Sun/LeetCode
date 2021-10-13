class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNum = nums[0]
        for i in range(1, len(nums)):
            # If the previous number + current number > current number
            # replace current number by the previous number + current number
            if nums[i-1] + nums[i] > nums[i]:
                nums[i] += nums[i-1]
            # if the current number is larger than the largest sum
            # replace the largest sum by the current number
            # because the sum of numbers are already stored in the current number
            if nums[i] > maxNum:
                maxNum = nums[i]
        return maxNum
                