def read_matrix(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    N, M = map(int, lines[0].split())
    matrix = [[int(x) for x in line.split()] for line in lines[1:]]
    return matrix


def find_max_in_column(matrix, column):
    max_element = -float("inf")
    for row in range(len(matrix)):
        if matrix[row][column] > max_element:
            max_element = matrix[row][column]

    return max_element


def get_column(matrix, column):
    column_vector = [matrix[i][column] for i in range(len(matrix))]
    return column_vector


def sum_positive_in_row(matrix, row):
    row_vector = [matrix[row][i] for i in range(len(matrix[row]))]
    positive_sum = sum(x for x in row_vector if x > 0)
    return positive_sum


def main():
    # Считать матрицу из файла
    matrix = read_matrix("matrix.txt")

    # Ввести число k
    k = int(input("Введите номер столбца: "))

    # Найти максимальный элемент в k-ом столбце
    max_element = find_max_in_column(matrix, k - 1)

    # Вырезать k-ый столбец из матрицы
    column_vector = get_column(matrix, k - 1)

    # Найти индекс строки, в которой находится максимальный элемент
    max_index = column_vector.index(max_element)

    # Найти сумму положительных элементов в строке с максимальным элементом
    positive_sum = sum_positive_in_row(matrix, max_index)

    # Вывести результаты
    print("Максимальный элемент в", k, "-ом столбце:", max_element)
    print("Сумма положительных элементов в строке с максимальным элементом:", positive_sum)


if __name__ == "__main__":
    main()
