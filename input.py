FILE_IN = "in.txt"


def get_matrix_from_file():
    # из файла
    with open(FILE_IN, 'rt') as fin:
        try:
            n = int(fin.readline())
            matrix = []
            for line in fin:
                new_row = list(map(float, line.strip().split()))
                if len(new_row) != (n + 1):
                    raise ValueError
                matrix.append(new_row)
            if len(matrix) != n:
                raise ValueError
        except ValueError:
            return None
    return matrix


def get_matrix_from_manual_input():
    # С клавиатуры
    while True:
        try:
            n = int(input("Порядок матрицы: "))
            if n <= 0:
                print("Порядок матрицы должен быть положительным.")
            else:
                break
        except ValueError:
            print("Порядок матрицы должен быть целым числом.")
    matrix = []
    print("Коэффициенты матрицы:")
    try:
        for i in range(n):
            matrix.append(list(map(float, input().strip().split())))
            if len(matrix[i]) != (n + 1):
                raise ValueError
    except ValueError:
        return None
    return matrix
