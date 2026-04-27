type List = List
from collections import deque
class Solution:
    def BFS(self, x:int, y:int, grid: List[List[str]], visited: List[List[bool]]) -> None:
        m, n = len(grid), len(grid[0])
        queue = deque([(x,y)])
        while queue:
            i, j = queue.popleft()
            visited[i][j] = True
            # children are above, below, left, right
            # 4 possible options (ugh)
            if i-1 >= 0 and not visited[i-1][j] and grid[i-1][j] == "1":
                queue.append((i-1, j))
            if i+1 < m and not visited[i+1][j] and grid[i+1][j] == "1":
                queue.append((i+1, j))
            if j+1 < n and not visited[i][j+1] and grid[i][j+1] == "1":
                queue.append((i, j+1))
            if j-1 >= 0 and not visited[i][j-1] and grid[i][j-1] == "1":
                queue.append((i, j-1))

    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * len(grid[0]) for i in range(len(grid))]
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == "1":
                    self.BFS(i, j, grid, visited)
                    ret += 1
                visited[i][j] = True
        return ret

if __name__ == '__main__':
    grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
    print(Solution().numIslands(grid))