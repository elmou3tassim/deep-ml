def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    if not a or not a[0] or len(a[0]) != len(b):
        return -1
    
    result = []
    for row in a:
        row_dot = sum(row[i] * b[i] for i in range(len(b)))
        result.append(row_dot)
        
    return result
	pass