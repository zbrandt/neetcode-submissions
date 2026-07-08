class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                print(num)
                if num != ".":
                    row_condition = num in rows[r]
                    column_condition = num in columns[c]
                    square_condition = num in squares[(r // 3, c // 3)]

                    if row_condition or column_condition or square_condition:
                        print(rows, columns, squares)
                        print(row_condition, column_condition, square_condition)
                        return False
                    
                    rows[r].add(num)
                    columns[c].add(num)
                    squares[(r // 3, c // 3)].add(num)

        return True
        