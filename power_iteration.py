import numpy as np

def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps

    Returns:
    eigenvalue: float – dominant eigenvalue estimation after `num_steps` steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """
    ### YOUR CODE HERE
    vect = np.ones(data.shape[1])

    for i in range(num_steps):
        vect_prev = vect
        vect = np.dot(data, vect) / np.linalg.norm(np.dot(data, vect))
        lambda_ = float((np.dot(vect_prev, np.dot(data, vect))) / (np.dot(vect_prev, vect_prev)))

    return lambda_, vect