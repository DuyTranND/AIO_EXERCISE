import numpy as np


def compute_vector_length(vector):
    """Calculate the Euclidean length of a given vector."""
    vector = np.array(vector)
    sum_of_squares = np.sum(vector**2)
    len_of_vector = np.sqrt(sum_of_squares)
    return len_of_vector


def compute_dot_product(vector1, vector2):
    """Calculate the dot product of two vector."""
    vector1, vector2 = np.array(vector1), np.array(vector2)
    result = np.sum(vector1*vector2)
    return result


def matrix_multi_vector(matrix, vector):
    """ Calculate the Multiplying a vector by a matrix."""
    matrix, vector = np.array(vector), np.array(matrix)
    result = np.dot(vector, matrix)
    return result


def matrix_multi_matrix(matrix1, matrix2):
    """ Calculate the Multiplying a matrix by a matrix."""
    matrix1, matrix2 = np.array(matrix1), np.array(matrix2)
    result = np.dot(matrix1, matrix2)
    return result


def inverse_matrix(matrix):
    """ Calculate the inverse of a matrix."""
    matrix = np.array(matrix)

    det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    if det != 0:
        inverse = (
            1 / det) * np.array([[matrix[1, 1], -matrix[0, 1]], [-matrix[1, 0], matrix[0, 0]]])
    else:
        print("Non-invertible")
    return inverse


def compute_eigenvalues_eigenvectors(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors


def compute_cosine(v1, v2):
    cos_sim = compute_dot_product(
        v1, v2) / (compute_vector_length(v1)*compute_vector_length(v2))
    return cos_sim


if __name__ == "__main__":
    """
    #Quiz1
    vector = np.array([-2, 4, 9, 21])
    result = compute_vector_length([vector])
    print(round(result, 2))

    #Quiz2
    v1 = np. array([0, 1, -1, 2])
    v2 = np. array([2, 5, 1, 0])
    result = compute_dot_product(v1, v2)
    print(round(result, 2))

    #Quiz3
    x = np. array([[1, 2],
                   [3, 4]])
    k = np. array([1, 2])
    print(x.dot(k))

    #Quiz4
    x = np. array([[-1, 2],
                   [3, -4]])
    k = np. array([1, 2])
    print(x@k)

    #Quiz5
    m = np. array([[-1, 1, 1], [0, -4, 9]])
    v = np. array([0, 2, 1])
    result = matrix_multi_vector(m, v)
    print(result)

    #Quiz6
    m1 = np. array([[0, 1, 2], [2, -3, 1]])
    m2 = np. array([[1, -3], [6, 1], [0, -1]])
    result = matrix_multi_matrix(m1, m2)
    print(result)

    #Quiz7
    m1 = np.eye(3)
    m2 = np. array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
    result = m1@m2
    print(m1)
    print(result)

    #Quiz8
    m1 = np.eye(2)
    m1 = np. reshape(m1, (-1, 4))[0]
    m2 = np. array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
    result = m1@m2
    print(result)

    #Quiz10
    m1 = np. array([[-2, 6], [8, -4]])
    result = inverse_matrix(m1)
    print(result)
    """
