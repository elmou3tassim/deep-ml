def matrixmul(a: list[list[int|float]], b: list[list[int|float]]) -> list[list[int|float]]:
    if not a or not b or len(a[0]) != len(b):
        return -1
    
    rowa = len(a)
    colsb = len(b[0])
    
    c = [[0] * colsb for _ in range(rowa)]
    
    for i in range(rowa):
        for j in range(colsb):
            c[i][j] = sum(a[i][k] * b[k][j] for k in range(len(b)))
            
    return c
