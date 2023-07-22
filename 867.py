matrix = [[1, 2, 3], [4, 5, 6]]


def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    res = [[""] * rows for i in range(columns)]

    for i in range(rows):
        row = []
        for j in range(columns):
            res[j][i] = matrix[i][j]
    return res


print(transpose(matrix))
