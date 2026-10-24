class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ''' 
        To solve it O(n**2) we can traverse entire grid and get result
        Optimization:
        Since the grid is sorted in each row as well as col to col,
        we can use a binary earch to find out which row we can find 
        the target and another binary serach to find out the existence 
        of that number in the row. If found return True, else False
        '''
        t, b = 0, len(matrix) - 1
        # binary search to find the ROW
        while t <= b:
            row = (t + b)//2
            if target > matrix[row][-1]:
                t = row + 1
            elif target < matrix[row][0]:
                b = row - 1
            else:
                break
        # if found that target is out of grid
        if not (t <=b):
            return False
        
        # second binary search to find in the ROW
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = (l + r)//2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        # if not found in that ROW
        return False
        