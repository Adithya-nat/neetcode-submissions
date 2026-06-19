class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        directions = [
            [1,0],
            [0,1],
            [-1,0],
            [0,-1]
        ]

        minutes = 0
        
        while fresh > 0 and queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for a,b in directions:
                    newr = r + a
                    newc = c + b

                    def withinGrid(r,c):
                        if 0 <= r < rows and 0 <= c < cols:
                            return True
                        return False
                    
                    if withinGrid(newr,newc) and grid[newr][newc] == 1 :
                        grid[newr][newc] = 2
                        queue.append((newr,newc))
                        fresh -= 1
                
            minutes += 1
        
        return minutes if fresh == 0 else -1



        