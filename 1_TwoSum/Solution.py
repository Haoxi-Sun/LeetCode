class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = {} # declare an empty dictionary
        
        for i in range(len(nums)):
            findNum = target - nums[i]
            # If 'findNum' in the dictionary,
            # the second number is founded,
            # return indexes
            if findNum in result.keys():
                return (result[findNum], i)
            # If 'findNum' not in the dictionary,
            # store the first number in the dictionary with index
            else:
                result[nums[i]] = i
        return result