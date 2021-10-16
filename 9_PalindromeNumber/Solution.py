class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = str(x) # covert integer to string
        
        # Reverse string 'num'.
        reversedNum = num
        reversedNum = reversedNum[::-1]
        # Compare the original string 'num' with the reversed string 'reversedNum'.
        for i in range(len(num)):
            if (num[i]) is not (reversedNum[i]):
                return False
        return True