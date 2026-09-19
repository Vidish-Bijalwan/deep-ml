def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	
    a, b = matrix[0]
    c, d = matrix[1]

    trace = a + d
    determinant = a * d - b * c

    discriminant = trace * trace - 4 * determinant

    root = discriminant ** 0.5

    eigenvalue1 = (trace + root) / 2
    eigenvalue2 = (trace - root) / 2

    return sorted([eigenvalue1, eigenvalue2], reverse=True)