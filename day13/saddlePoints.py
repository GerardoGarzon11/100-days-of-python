def matrixIsValid(matrix):
	if len(matrix) < 1:
		return True

	firstRowLen = len(matrix[0])

	for x in matrix:
		if len(x) != firstRowLen:
			return False

	return True

def saddle_points(matrix):
	if not matrixIsValid(matrix):
		raise ValueError("Matrix is not valid")

	saddle_points = []

	# rows
	for x_index, x in enumerate(matrix):
		# cols
		for y_index, y in enumerate(x):
			col = [x[y_index] for x in matrix]
			if y == max(x) and y == min(col):
				saddle_points.append({"row" : x_index + 1, "column": y_index + 1})

	return [{}] if not saddle_points else saddle_points
