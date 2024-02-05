class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        depth = len(matrix)
        width = len(matrix[0])
        for i in range(depth-1):
            if(matrix[i][0] <= target and matrix[i+1][0] > target):
                for j in range(width):
                    if(matrix[i][j] == target):
                        return True
                return False
        for j in range(width):
            if(matrix[-1][j] == target):
                return True
        return False

