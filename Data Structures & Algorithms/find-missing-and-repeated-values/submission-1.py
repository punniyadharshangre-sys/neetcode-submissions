class Solution:
    def find_missing(self,elements):
        i,j=0,1
        if elements[i]!=1:
            return 1
        while j<len(elements):
            if elements[i]+1!=elements[j]:
                return elements[i]+1
            i+=1
            j+=1
        if len(elements)!=self.size:
            return elements[-1]+1
        
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        elements=[]
        missing,repeated=None,None
        self.size=len(grid[0])*len(grid)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] in elements:
                    repeated=grid[i][j]
                else:
                    elements.append(grid[i][j])
        print(sorted(elements))
        missing=self.find_missing(sorted(elements))
        return [repeated,missing]
        

        