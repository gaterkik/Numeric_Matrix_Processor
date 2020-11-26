import numpy


def show_menu():
    print('')
    print('1. Add matrices')
    print('2. Multiply matrix by a constant')
    print('3. Multiply matrices')
    print('0. Exit')
    user_choice = input('Your choice:')
    if user_choice == '1':
        add_matrices()
    if user_choice == '2':
        multiply_matrix_by_const()
    if user_choice == '3':
        multiply_matrices()
    if user_choice == '0':
        pass


def add_matrices():
    print('Enter size of first matrix:')
    m1, n1 = (int(i) for i in input().split(' '))
    print('Enter first matrix:')
    a1 = input_matrix(m1, n1)
    print('Enter size of second matrix:')
    m2, n2 = (int(i) for i in input().split(' '))
    print('Enter second matrix')
    a2 = input_matrix(m2, n2)
    print('The result is:')
    print_matrix(a1 + a2)
    show_menu()


def multiply_matrix_by_const():
    print('Enter size of matrix:')
    m, n = (int(i) for i in input().split(' '))
    a = input_matrix(m, n)
    c = float(input('Enter constant:'))
    print('The result is:')
    print_matrix(a * c)
    show_menu()


def multiply_matrices():
    print('Enter size of first matrix:')
    m1, n1 = (int(i) for i in input().split(' '))
    print('Enter first matrix:')
    a1 = input_matrix(m1, n1)
    print('Enter size of second matrix:')
    m2, n2 = (int(i) for i in input().split(' '))
    print('Enter second matrix')
    a2 = input_matrix(m2, n2)
    print('The result is:')
    print_matrix(numpy.dot(a1, a2))
    show_menu()


def input_matrix(m, n):
    l1 = []
    for i in range(m):
        # l1.append(input().split(' '))
        l1.append(list(float(item) for item in input().split(' ')))
        # array[i] = [item for item in input().split(' ')]
        # print(l1)

    array = numpy.array(l1)
    # print(array)
    return array


def print_matrix(matrix):
    m, n = matrix.shape
    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print()

# print_matrix(input_matrix(2, 2))
show_menu()
