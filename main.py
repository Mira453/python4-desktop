import numpy as np

def is_reflexive(matrix):
    for i in range(len(matrix)):
        if matrix[i][i] != 1:
            return False
    return True

def is_symmetric(matrix):
    return np.array_equal(matrix, matrix.T)

def is_transitive(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if matrix[i][j] == 1 and matrix[j][k] == 1 and matrix[i][k] != 1:
                    return False
    return True

def is_equivalence_relation(matrix):
    return is_reflexive(matrix) and is_symmetric(matrix) and is_transitive(matrix)

def is_partial_order(matrix):
    return is_reflexive(matrix) and is_transitive(matrix) and not is_symmetric(matrix)

def is_strict_order(matrix):
    return not is_reflexive(matrix) and not is_symmetric(matrix) and is_transitive(matrix)

def transitive_closure(matrix):
    n = len(matrix)
    closure = matrix.copy()
    for k in range(n):
        for i in range(n):
            for j in range(n):
                closure[i][j] = closure[i][j] or (closure[i][k] and closure[k][j])
    return closure

def symmetric_closure(matrix):
    return np.maximum(matrix, matrix.T)

def matrix_power(matrix, power):
    result = np.linalg.matrix_power(matrix, power)
    return (result > 0).astype(int)

def main():
    matrix = np.array([
        [0, 1, 1, 1, 1],
        [1, 0, 0, 1, 0],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1]
    ])

    print("Початкова матриця:")
    print(matrix)

    print("\nВластивості відношення:")
    print("Рефлексивність:", is_reflexive(matrix))
    print("Симетричність:", is_symmetric(matrix))
    print("Транзитивність:", is_transitive(matrix))
    print("Відношення еквівалентності:", is_equivalence_relation(matrix))
    print("Частковий порядок:", is_partial_order(matrix))
    print("Суворий порядок:", is_strict_order(matrix))

    transitive_closure_matrix = transitive_closure(matrix)
    symmetric_closure_matrix = symmetric_closure(matrix)

    print("\nТранзитивне замикання:")
    print(transitive_closure_matrix)

    print("\nСиметричне замикання:")
    print(symmetric_closure_matrix)

    second_power = matrix_power(matrix, 2)
    third_power = matrix_power(matrix, 3)

    print("\nДругий степінь відношення:")
    print(second_power)

    print("\nТретій степінь відношення:")
    print(third_power)

if __name__ == "__main__":
    main()