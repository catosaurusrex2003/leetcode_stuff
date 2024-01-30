board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


def isValidSudoku(board):
    # checking row
    for i in range(9):
        track = {}
        for j in range(9):
            if board[i][j] != ".":
                if board[i][j] in track:
                    # print(track)
                    # print(board[i][j])
                    # print(f"false row found in {i} {j}")
                    return False
                else:
                    track[board[i][j]] = 1
    # checking col
    for i in range(9):
        track = {}
        for j in range(9):
            if board[j][i] != ".":
                if board[j][i] in track:
                    # print(track)
                    # print(board[j][i])
                    # print(f"false col found in {i} {j}")
                    return False
                else:
                    track[board[j][i]] = 1
    # per grid
    for i in range(9):
        startRow = (i // 3) * 3
        startCol = (i % 3) * 3
        track = {}
        for j in range(9):
            localStartRow = (j // 3) + startRow
            localStartCol = (j % 3) + startCol
            if board[localStartRow][localStartCol] != ".":
                # print(localStartRow, localStartCol)
                if board[localStartRow][localStartCol] in track:
                    # print(track)
                    # print(board[localStartRow][localStartCol])
                    # print(f"false grid found in {i} {j}")
                    return False
                else:
                    track[board[localStartRow][localStartCol]] = 1
    return True


something = isValidSudoku(board)
print(something)


# for i in range(9):
#     startRow = (i // 3) * 3
#     startCol = (i % 3) * 3
#     track = {}
#     for j in range(9):
#         localStartRow = (j // 3) + startRow
#         localStartCol = (j % 3) + startCol
#         print(localStartRow, localStartCol)
