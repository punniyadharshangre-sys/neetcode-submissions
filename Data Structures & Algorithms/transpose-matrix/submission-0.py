class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows=len(matrix)
        column=len(matrix[0])
        ans=[[0]*rows for i in range(column)]
        for r in range(rows):
            for c in range(column):
                if r==c:
                    ans[r][c]=matrix[r][c]
                else:
                    ans[c][r]=matrix[r][c]
        return ans
