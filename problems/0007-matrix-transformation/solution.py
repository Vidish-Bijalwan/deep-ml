import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:

	A = np.array(A,dtype =float)
	T = np.array(T,dtype =float)
	S = np.array(S,dtype = float)

	if np.linalg.det(T) == 0 or np.linalg.det(S) ==0:
		return -1
	T_inverse = np.linalg.inv(T)

	transformed_matrix = T_inverse@A@S

	return transformed_matrix.tolist()