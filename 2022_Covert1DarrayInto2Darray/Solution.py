class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        List = []
        if m * n == len(original):
            copy = original
            for i in range(m):
                col = []
                for j in range(n):
                    col.insert(j,copy[j])
                List.insert(i,col)
                del copy[:n]
            return(List)
        else:
            return(List)