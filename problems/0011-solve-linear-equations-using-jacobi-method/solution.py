import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	
	x = np.zeros(len(b))
	for _ in range(n):
		x_new = np.zeros(len(A))
		for i in range(len(A)):
			total = 0
			for j in range(len(A)):
				if i !=j:
					total+= A[i][j] * x[j]
			x_new[i] = (b[i]- total) / A[i][i]
		x = x_new
	return x.tolist()
			