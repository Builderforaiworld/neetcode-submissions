class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left=0
        right=len(matrix)-1
        while (left<=right):
            mid=(left+right)//2
            if target>matrix[mid][-1]:
                left=mid+1
            elif target<matrix[mid][0]:
                right=mid-1
            else:
                break
        l=0
        r=len(matrix[0])-1
        while (l<=r):
            mid_col=(l+r)//2
            if target==matrix[mid][mid_col]:
                return True
            elif target>matrix[mid][mid_col]:
                l=mid_col+1
            else:
                r=mid_col-1
        return False
            
