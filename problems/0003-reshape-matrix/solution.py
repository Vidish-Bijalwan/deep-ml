import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:

	flat = []

	for row in a:
		for value in row:
			flat.append(value)
	
	new_rows = new_shape[0]
	new_cols = new_shape[1]

	if len(flat) != new_rows * new_cols:
		return []
	
	result  = []
	index = 0

	for i in range(new_rows):
		new_row = []

		for j in range(new_cols):
			new_row.append(flat[index])
			index +=1
		result.append(new_row)
	
	reshaped_matrix = result
	
	return reshaped_matrix