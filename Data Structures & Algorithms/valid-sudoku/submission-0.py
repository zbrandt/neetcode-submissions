class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

        # check rows
        for row in board:
            nums = set()
            row = [s.strip() for s in row]
            for num in row:
                if num in valid and num in nums:
                    return False
                nums.add(num)
        
        # check columns
        for c in range(len(board[0])):
            nums = set()
            for r in range(len(board)):
                num = board[r][c].strip()
                if num in valid and num in nums:
                    return False
                nums.add(num)

        # check squares
        for square in range(9):
            nums = set()
            for row in range((square // 3) * 3, (square // 3) * 3 + 3):
                for col in range((square % 3) * 3, (square % 3) * 3 + 3):
                    num = board[row][col].strip()
                    print(num)
                    print(nums)
                    if num in valid and num in nums:
                        return False
                    nums.add(num)
            print(nums)
        return True

        