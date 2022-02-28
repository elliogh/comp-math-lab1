from solve import print_matrix


# Getting the matrix from user
def get_matrix():
    new_matrix = []
    print('Лабораторная работа #1, вариант 23, Целиков Данил P3212')
    print('Выберите режим: 0 - взять коэффициенты из файла, 1 - ввести коэффициенты с клавиатуры')
    answer = int(input())
    if answer == 1:
        print('Размер матрицы?')
        rows = int(input())

        if rows != 1:
            for i in range(rows):
                a = []
                for j in range(rows + 1):
                    print('Элемент: строка', i + 1, ', столбец:', j + 1)
                    a.append(float(input()))
                new_matrix.append(a)
            print('Ваша матрица:')
            print(new_matrix)
            return new_matrix
        else:
            print('Матрица должна быть 2x2, 3x3 ... 20x20! Попытайтесь еще!')
            return get_matrix()
    elif answer == 0:
        print('Пожалуйста, введите имя вашего файла!')
        return get_matrix_from_file(input())
    else:
        print('Что-то не так! Попытайтесь еще!')
        return get_matrix()


# Getting matrix from the file by filename
def get_matrix_from_file(filename):
    with open(filename) as f:
        matrix_from_file = [list(map(float, row.split())) for row in f.readlines()]
    print('Матрица:')
    print_matrix(matrix_from_file, 5)
    return matrix_from_file
