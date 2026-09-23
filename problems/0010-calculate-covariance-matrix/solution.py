def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    n_features = len(vectors)
    n = len(vectors[0])

    means = [sum(feature) / n for feature in vectors]

    matrix = []

    for i in range(n_features):
        row = []

        for j in range(n_features):
            covariance = 0

            for k in range(n):
                covariance += (
                    (vectors[i][k] - means[i]) *
                    (vectors[j][k] - means[j])
                )

            covariance /= (n - 1)
            row.append(covariance)

        matrix.append(row)   

    return matrix