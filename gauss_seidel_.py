
import numpy as np

def gauss_seidel(A, b, tol, max_iteracoes):
    n = len(A)

    # Verificar se a matriz A é quadrada
    if A.shape[0] != A.shape[1]:
        print("A matriz A não é quadrada. O sistema pode não ter uma solução única.")
        return None

    # Verificar se o número de linhas de A é igual ao número de elementos em b
    if A.shape[0] != len(b):
        print("O número de linhas da matriz A é diferente do número de elementos em b.")
        return None

    # Verificar se a diagonal principal de A é dominante
    if not np.all(np.abs(np.diag(A)) >= np.sum(np.abs(A), axis=1) - np.abs(np.diag(A))):
        print("A matriz A não possui diagonal dominante. Os métodos podem não convergir.")

    # Verificar convergência para o método de Gauss-Seidel
    if np.linalg.norm(A, np.inf) >= 1:
        print("O método de Gauss-Seidel pode não convergir para esse sistema.")

    # Verificar convergência para o método de Jacobi
    if np.linalg.norm(A, np.inf) >= 1 / (1 - np.linalg.norm(A - np.diag(np.diag(A)), np.inf)):
        print("O método de Jacobi pode não convergir para esse sistema.")

    x = np.zeros(n)  # vetor inicial
    iteracoes = 0

    while iteracoes < max_iteracoes:
        x_prev = x.copy()

        for i in range(n):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1:], x_prev[i+1:])) / A[i, i]

        if np.linalg.norm(x - x_prev, np.inf) < tol:
            print("Convergência alcançada após", iteracoes+1, "iterações.")
            return x

        iteracoes += 1

    print("Não foi alcançada convergência após", max_iteracoes, "iterações.")
    return x

# Exemplo de uso
A = np.array([[10, 2, -1], [1, 5, 1], [2, -3, 10]])
b = np.array([27, -8, 23])
tolerancia = 1e-6
maximo_iter = 100

solucao = gauss_seidel(A, b, tolerancia, maximo_iter)
if solucao is not None:
    print("Solução encontrada:", solucao)

