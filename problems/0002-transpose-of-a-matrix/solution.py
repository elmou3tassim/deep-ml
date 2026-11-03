def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    if not a or not a[0]:
        return []
    
    row, col = len(a), len(a[0])
    b = [[0] * row for _ in range(col)]
    
    for i in range(row):
        for j in range(col):
            b[j][i] = a[i][j]
            
    return b

    pass