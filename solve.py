# Realising a Gauss's Method
def do_gauss_method(input_matrix):
    check_square_matrix(input_matrix)
    print('Метод Гаусса')
    length_of_matrix = len(input_matrix)
    do_triangle_matrix(input_matrix)
    is_singular(input_matrix)
    input_answer_matrix = [0 for i in range(length_of_matrix)]

    for k in range(length_of_matrix - 1, -1, -1):
        input_answer_matrix[k] = (input_matrix[k][-1] - sum(
            [input_matrix[k][j] * input_answer_matrix[j] for j in range(k + 1, length_of_matrix)])) / input_matrix[k][k]

    print('Ответы!')
    for i in range(len(input_answer_matrix)):
        print('x[', i + 1, '] =', "%5.3f" % input_answer_matrix[i])
    return input_answer_matrix


# Checking the matrix
def check_square_matrix(input_matrix):
    print('Проверка квадратная ли матрица и имеет ли она решения')
    for i in range(len(input_matrix)):
        if len(input_matrix) + 1 != len(input_matrix[i]):
            raise Exception('ERROR: Неправильный размер матрицы')
        count = 0
        for j in range(len(input_matrix[i]) - 1):
            if input_matrix[i][j] == 0:
                count += 1
        if count == len(input_matrix[i]) - 1:
            raise Exception('ERROR: у матрицы нет решений')
    print('Все в порядке!')


def do_triangle_matrix(input_matrix):
    print('Сделаем треугольную матрицу')
    length_of_matrix = len(input_matrix)  # = number of rows

    for k in range(length_of_matrix - 1):
        print('Итерация №', k + 1)
        print('Матрица была...')
        print_matrix(input_matrix, 5)
        get_max_element_in_column(input_matrix, k)
        print('Матрица стала ...')
        print_matrix(input_matrix, 5)

        print('Преобразование...')

        for i in range(k + 1, length_of_matrix):
            div = input_matrix[i][k] / input_matrix[k][k]
            input_matrix[i][-1] -= div * input_matrix[k][-1]
            for j in range(k, length_of_matrix):
                input_matrix[i][j] -= div * input_matrix[k][j]
        print_matrix(input_matrix, 5)
    return length_of_matrix


# Checking if matrix is singular (вырожденная)
def is_singular(input_matrix):
    print('Проверка вырожденная ли матрица')
    if count_determinant_for_square_matrix(input_matrix) == 0:
        raise Exception('ERROR: Ваша матрица вырожденная (det ~ 0)')
    else:
        print('Ваша матрица не вырожденная')


# Searching for the main element in the column
def get_max_element_in_column(input_matrix, number_of_column):
    max_element = input_matrix[number_of_column][number_of_column]
    max_row = number_of_column
    for j in range(number_of_column + 1, len(input_matrix)):
        if abs(input_matrix[j][number_of_column]) > abs(max_element):
            max_element = input_matrix[j][number_of_column]
            max_row = j
    if max_row != number_of_column:
        input_matrix[number_of_column], input_matrix[max_row] = input_matrix[max_row], input_matrix[number_of_column]
    print('Максимальный элемент - ', "%.4f" % max_element, 'в строке', max_row + 1)
    return input_matrix


# Printing matrix in the comfortable view
def print_matrix(input_matrix, decimals):
    for i in range(len(input_matrix)):
        for j in range(len(input_matrix[i])):
            print('|', "%10.4f" % (input_matrix[i][j]), end=' ')
        print()


# Create residual vector (вектор невязок)
def do_residual_vector(input_matrix, input_answer_matrix):
    big_matrix = []
    little_matrix = []
    for i in range(len(input_matrix)):
        big_matrix.append(input_matrix[i][0:len(input_matrix)])
        little_matrix.append(input_matrix[i][len(input_matrix):])
    x_matrix = input_answer_matrix
    temp = [0 for i in range(len(input_matrix))]
    residual_vector = [0 for i in range(len(input_matrix))]

    print('Вектор невязок:')
    for i in range(len(big_matrix)):
        temp[i] = 0
        for j in range(len(big_matrix)):
            temp[i] += x_matrix[j] * big_matrix[i][j]
        residual_vector[i] = temp[i] - little_matrix[i][0]
        print('r[', i + 1, '] =', residual_vector[i], end='\n')


# Counting the determinant of the out matrix
def count_determinant_for_square_matrix(input_matrix):
    determinant = 1
    for i in range(len(input_matrix)):
        determinant *= input_matrix[i][i]
    print('Определитель матрицы =', round(determinant, 5))
    return round(determinant, 5)
