def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    a = matrix[0][0]
    c = matrix[0][1]
    b = matrix[1][0]
    d = matrix[1][1]
    
    trace=a+d
    det=a*d-b*c
    
    delta =(trace**2-4*det)**0.5
    
    return[(trace+delta)/2,(trace-delta)/2]
