import numpy as np


def compute_vector_length(vector):
    """Calculate the Euclidean length of a given vector."""
    norm = np.linalg.norm(vector)
    return norm


def compute_dot_product(vector1, vector2):
    """Calculate the dot product of two vector."""
    vector1, vector2 = np.array(vector1), np.array(vector2)
    result = np.sum(vector1@vector2)
    return result


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
