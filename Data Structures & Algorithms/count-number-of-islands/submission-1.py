class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        islands = 0

        directions = [
                        (-1, 0),
                        (1, 0),
                        (0, -1),
                        (0, 1)
                    ]


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "0" or (row, col) in visited:
                    continue
                
                visited.add((row, col))
                islands += 1
                stack = [(row, col)]

                while stack:
                    cur_row, cur_col = stack.pop()

                    for a, b in directions:
                        new_row = cur_row + a
                        new_col = cur_col + b

                        if( new_row >= 0 and new_row < rows and new_col >=0 and new_col < cols and grid[new_row][new_col] == "1" and (new_row, new_col) not in visited ):
                            visited.add((new_row, new_col))
                            stack.append((new_row, new_col))
                
        return islands





        