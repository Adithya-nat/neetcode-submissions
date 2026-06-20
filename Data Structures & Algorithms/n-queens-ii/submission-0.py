class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        d1 = set()
        d2 = set()
        count = 0

        def backtrack(row):
            nonlocal count
            if row == n:
                count += 1
                return
            
            for c in range(n):
                if c in cols or row - c in d1 or row + c in d2:
                    continue
                
                cols.add(c)
                d1.add(row-c)
                d2.add(row+c)

                backtrack(row+1)

                cols.remove(c)
                d1.remove(row-c)
                d2.remove(row+c)
            
        
        backtrack(0)
        return count

        