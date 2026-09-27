def determinant_4x4(matrix: list[list[int | float]]) -> float:
    def det(m):
        if len(m) == 1:
            return m[0][0]
        if len(m) == 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]

        result = 0
        for j in range(len(m)):
            minor = [row[:j] + row[j + 1:] for row in m[1:]]
            result += (-1) ** j * m[0][j] * det(minor)

        return result

    return det(matrix)