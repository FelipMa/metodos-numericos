import numpy as np

def gauss_jacobi(A, b, x0, max_iterations=100, tolerance=1e-6):
    n = len(A)
    x = x0.copy()
    for _ in range(max_iterations):
        x_new = x.copy()
        for i in range(n):
            sum_ax = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_ax) / A[i][i]
        if all(abs(x_new[i] - x[i]) < tolerance for i in range(n)):
            return x_new
        x = x_new
    return None


def gauss_seidel(A, b, x0, max_iterations=100, tolerance=1e-6):
    n = len(A)
    x = x0.copy()
    for _ in range(max_iterations):
        x_new = x.copy()
        for i in range(n):
            sum_ax = sum(A[i][j] * x_new[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sum_ax) / A[i][i]
        if all(abs(x_new[i] - x[i]) < tolerance for i in range(n)):
            return x_new
        x = x_new
    return None


def get_matrix_input(size):
    matrix = []
    print("Elementos da matriz:")
    for i in range(size):
        row = list(map(float, input().split()))
        matrix.append(row)
    return matrix


def get_vector_input(size):
    vector = []
    print("Elementos do Vetor:")
    vector = list(map(float, input().split()))
    return vector


def main():
    size = int(input("Tamanho da matriz: "))
    A = get_matrix_input(size)
    b = get_vector_input(size)

    # Verifying if the matrix A is invertible
    if np.linalg.det(A) == 0:
        print("The matrix A is not invertible. The system may not have a unique solution.")
        return

    x0 = [0] * size  # Initial guess
    max_iterations = int(input("Enter the maximum number of iterations: "))
    tolerance = float(input("Enter the tolerance: "))

    solution_jacobi = gauss_jacobi(A, b, x0, max_iterations, tolerance)
    solution_seidel = gauss_seidel(A, b, x0, max_iterations, tolerance)

    if solution_jacobi is None:
        print("The Jacobi method did not converge.")
    else:
        # Verifying if the solution is unique
        augmented_matrix = np.column_stack((A, b))
        rank_A = np.linalg.matrix_rank(A)
        rank_augmented = np.linalg.matrix_rank(augmented_matrix)
        if rank_A == rank_augmented and rank_A == size:
            print("The system has a unique solution.")
        else:
            print("The system may not have a unique solution.")

        print("The solution using Jacobi method is:")
        for i, value in enumerate(solution_jacobi):
            print(f"x{i+1} =", value)

    if solution_seidel is None:
        print("The Gauss-Seidel method did not converge.")
    else:
        print("The solution using Gauss-Seidel method is:")
        for i, value in enumerate(solution_seidel):
            print(f"x{i+1} =", value)

    if solution_jacobi is not None and solution_seidel is not None:
        print("Both Jacobi and Gauss-Seidel methods converged.")
    elif solution_jacobi is not None:
        print("Only Jacobi method converged.")
    elif solution_seidel is not None:
        print("Only Gauss-Seidel method converged.")


if __name__ == '__main__':
    main()
