tRow = (i // 3) * 3
    startCol = (i % 3) * 3
    track = {}
    for j in range(9):
        localStartRow = (i // 3) + startRow
        localStartCol = (i % 3) + startCol
        print(localStartRow, localStartCol)