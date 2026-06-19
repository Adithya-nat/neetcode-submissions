class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        shapes = set()

        directions = [[-1,0], [1,0], [0,1], [0,-1]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 or (r,c) in visited:
                    continue
                startr=r
                startc=c
                visited.add((r,c))
                stack = [(r,c)]
                shape = []

                while stack:
                    curr, curc = stack.pop()

                    shape.append((curr-startr, curc-startc))



                    for a,b in directions:
                        newr = curr+a
                        newc = curc+b
                        if 0 <= newr < rows and 0 <= newc < cols and grid[newr][newc] == 1 and (newr, newc) not in visited :
                            stack.append((newr, newc))
                            visited.add((newr, newc))
                
                shapes.add(tuple(sorted(shape)))
            
        return len(shapes)

                


        