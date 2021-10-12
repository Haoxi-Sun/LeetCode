# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Using the binary search tree
        left = 1
        while left <= n:
            # Calculate middle numer in the binary tree 'mid = low + (high - low) / 2'
            mid = left + (n-left)//2
            if guess(mid) == 0: return(mid)
            # If the picked number is lower than your guess
            # the picked number is between 1 and mid.
            if guess(mid) == -1: n = mid - 1
            # If the picked number is higher than you guess
            # the picked number is between mid and n. 
            if guess(mid) == 1:left = mid + 1 
            