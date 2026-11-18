
class Solution:
    def __init__(self):
        self.visited = set()
    def dfs(self,node,isConnected):
        self.visited.add(node)
        n=len(isConnected[node])
        for neighbor in range(n):
            if isConnected[node][neighbor] == 1 and neighbor not in self.visited:
                self.dfs(neighbor,isConnected)
    


    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        n=len(isConnected)
        for i in range(n):
            if i not in self.visited:
                self.dfs(i,isConnected)
                count += 1
        return count
        