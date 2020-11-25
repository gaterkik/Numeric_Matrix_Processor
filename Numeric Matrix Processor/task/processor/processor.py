import numpy


def input_matrix():
    m, n = (int(i) for i in input().split(' '))
    array = numpy.zeros((m, n))
    for i in range(m):
        array[i] = list((int(item) for item in input().split(' ')))
    return array


def print_matrix(matrix):
    m, n = matrix.shape
    for i in range(m):
        for j in range(n):
            print(int(matrix[i][j]), end=' ')
        print()

a = input_matrix()
# print_matrix(a)
b = input_matrix()

if a.shape == b.shape:
    print_matrix(a + b)
else:
    print('ERROR')

# print(a)