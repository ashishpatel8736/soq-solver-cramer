import numpy as np

def solve_cramers_rule(coeff_matrix, const_vector):
    """
    Solves a system of linear equations using Cramer's Rule.

    Parameters:
    coeff_matrix (list of list of floats): The coefficient matrix of the system.
    const_vector (list of floats): The constant terms vector.

    Returns:
    list or str: Solution vector (values of variables) or an error message.
    """
    coeff_matrix = np.array(coeff_matrix, dtype=float)
    const_vector = np.array(const_vector, dtype=float)

    # Check if the matrix is square
    if coeff_matrix.shape[0] != coeff_matrix.shape[1]:
        return "Error: Coefficient matrix must be square."

    # Calculate the determinant of the coefficient matrix
    det_main = np.linalg.det(coeff_matrix)
    
    # If determinant is zero, the system does not have a unique solution
    if np.isclose(det_main, 0):
        return "No unique solution exists (determinant is zero)."

    # Solve for each variable using Cramer's Rule
    num_vars = coeff_matrix.shape[1]
    solution = []
    for i in range(num_vars):
        # Replace the i-th column of the coefficient matrix with the constant vector
        modified_matrix = coeff_matrix.copy()
        modified_matrix[:, i] = const_vector
        # Calculate the determinant of the modified matrix
        det_modified = np.linalg.det(modified_matrix)
        # Solve for the i-th variable
        solution.append(round(det_modified / det_main, 6))  # Round for cleaner output

    return solution
