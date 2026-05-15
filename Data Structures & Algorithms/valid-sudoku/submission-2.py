class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, columns = len(board), len(board[0])
        #rows
        for i in range(rows):
            track = set()
            for c in range(columns):
                if board[i][c] != ".":
                    if board[i][c] not in track:
                        track.add(board[i][c])
                    else:
                        return False
        #columns
        for i in range(columns):
            track = set()
            for c in range(rows):
                if board[c][i] != ".":
                    if board[c][i] not in track:
                        track.add(board[c][i])
                    else:
                        return False
        #boxes
        dr = 0
        dc = 0
        for _ in range(3):
            for _ in range(3):
                track = set()
                for r in range(3):
                    for c in range(3):
                        if board[dr + r][dc + c] != ".":
                            if board[dr + r][dc + c] not in track:
                                track.add(board[dr + r][dc + c])
                            else:
                                return False
                dr += 3
            dr = 0
            dc += 3
        return True


        