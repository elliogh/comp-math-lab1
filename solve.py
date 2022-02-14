def solve_minor(matrix, i, j):
    n = len(matrix)
    return [[matrix[row][col] for col in range(n) if col != j] for row in range(n) if row != i]


def find_det(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    det = 0
    sgn = 1
    for j in range(n):
        det += sgn * matrix[0][j] * find_det(solve_minor(matrix, 0, j))
        sgn *= -1
    return det


def solve(matrix):
    n = len(matrix)
    det = find_det([matrix[i][:n] for i in range(n)])
    if det == 0:
        return None

    # Прямой ход
    for i in range(n - 1):
        # Поиск максимального элемента в столбце
        max_l = i
        for m in range(i + 1, n):
            if abs(matrix[m][i]) > abs(matrix[max_l][i]):
                max_l = m

        # Перестановка строк
        if max_l != i:
            for j in range(n + 1):
                matrix[i][j], matrix[max_l][j] = matrix[max_l][j], matrix[i][j]

        # Исключение i-того неизвестного
        for k in range(i + 1, n):
            coif = matrix[k][i] / matrix[i][i]
            for j in range(i, n + 1):
                matrix[k][j] -= coif * matrix[i][j]

    reduced_matrix = matrix[:]

    # Обратный ход
    roots = [0] * n
    for i in range(n - 1, -1, -1):
        s_part = 0
        for j in range(i + 1, n):
            s_part += matrix[i][j] * roots[j]
        roots[i] = (matrix[i][n] - s_part) / matrix[i][i]

    # Вычисление невязок
    residuals = [0] * n
    for i in range(n):
        s_part = 0
        for j in range(n):
            s_part += matrix[i][j] * roots[j]
        residuals[i] = s_part - matrix[i][n]

    return det, reduced_matrix, roots, residuals
