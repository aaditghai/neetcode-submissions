class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, columns = len(board), len(board[0])
        row, column = defaultdict(set), defaultdict(set)
        squares = defaultdict(set)
        for r in range(rows):
            for c in range(columns):
                if board[r][c] == ".":
                    continue
                if board[r][c] in row[r] or board[r][c] in column[c] or board[r][c] in squares[(r//3, c//3)]:
                    return False
                row[r].add(board[r][c])
                column[c].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True
        