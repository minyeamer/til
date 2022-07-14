class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        
        for i in range(len(mat)):
            mat[i] = [i, sum(mat[i])]

        mat.sort(key=lambda x: x[1])
        print(mat)

        return [mat[i][0] for i in range(k)]
