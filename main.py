import input as en
from solve import solve


def main():
    print("\t\tЛабораторная работа #1, вариант 23, Целиков Данил P3212")
    print("Выберите режим: 0 - взять коэффициенты из файла, 1 - ввести коэффициенты с клавиатуры")

    method = input(">>> ")
    while (method != '0') and (method != '1'):
        print("Введите '0' или '1' для выбора способа ввода.")
        method = input(">>> ")

    if method == '0':
        matrix = en.get_matrix_from_file()
    else:
        matrix = en.get_matrix_from_manual_input()

    if matrix is None:
        print("При считывании коэффициентов матрицы произошла ошибка!")
        return

    answer = solve(matrix[:])
    if answer is None:
        print("\nМатрица является несовместной.")
        return
    det, reduced_matrix, roots, residuals = answer

    print("\nОпределитель:")
    print(det)

    print("\nПреобразованная матрица:")
    for row in reduced_matrix:
        for col in row:
            print('{:10}'.format(round(col, 3)), end='')
        print()

    print("\nВектор неизвестных:")
    for root in roots:
        print('  ' + str(root))

    print("\nВектор невязок:")
    for residual in residuals:
        print('  ' + str(residual))


if __name__ == '__main__':
    main()
