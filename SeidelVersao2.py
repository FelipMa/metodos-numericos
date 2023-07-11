def seidel(A, b, tol=1e-6, maxIt=100):
    # A = matriz de coeficientes
    # b = vetor de termos independentes
    n = len(A) # tamanho da matriz (n x n)
    x = [0] * n # chute inicial (um vetor de zeros)
    x_new = x.copy()

    for _ in range(maxIt): # iterações
        for i in range(n): # para cada linha
            elem = [] # lista que irá guardar A[i][j] * x[j]

            for j in range(n): # para cada elemento da linha atual (coluna)
                if j != i: # se não for a diagonal
                    elem.append(A[i][j] * x_new[j]) # multiplica elemento da linha por elemento do chute atualizado, e adiciona na lista de elementos

            x_new[i] = (b[i] - sum(elem)) / A[i][i] # calcula o novo valor de x, e adiciona na lista de novos valores de x

        estaNaTolerancia = True # flag para verificar se todos os elementos de x_new estão na tolerância

        dif = [] # lista que irá guardar as diferenças absolutas entre x(k) e x(k-1)
        for i in range(n):
            dif.append(abs(x_new[i] - x[i])) # calcula a diferença entre x(k) e x(k-1) e adiciona na lista de diferenças

        x_abs = [] # lista que irá guardar os valores absolutos de x(k)
        for i in range(n):
            x_abs.append(abs(x_new[i]))

        er = max(dif) / max(x_abs) # calcula o erro relativo

        if er > tol: # se o erro relativo for maior que a tolerância, x_new não está na tolerância
            estaNaTolerancia = False
        
        if estaNaTolerancia: # se x_new está na tolerância, retorna x_new
            return x_new
        else:
            x = x_new.copy() # se não, x = x_new, e continua o loop

    return x_new # retorna x_new se o número máximo de iterações for atingido (para vermos onde a iteração parou)

def convergenciaLinhas(A):
    # verifica se a matriz A é diagonalmente dominante por linhas
    # se for, retorna True, se não, retorna False
    n = len(A)
    for i in range(n):
        soma = 0
        for j in range(n):
            if i != j:
                soma += abs(A[i][j])
        if abs(A[i][i]) < soma:
            return False
    return True

def convergenciaColunas(A):
    # verifica se a matriz A é diagonalmente dominante por colunas
    # se for, retorna True, se não, retorna False
    n = len(A)
    for i in range(n):
        soma = 0
        for j in range(n):
            if i != j:
                soma += abs(A[j][i])
        if abs(A[i][i]) < soma:
            return False
    return True

def criterioSassenfeld(A):
    # verifica se a matriz A atende ao critério de Sassenfeld
    # se atender, retorna True, se não, retorna False
    n = len(A)
    beta = [1] * n # vetor de betas começa com 1 em todas as posições
    for i in range(n):
        soma = 0
        for j in range(n):
            if i != j:
                soma += beta[j] * (abs(A[i][j]) / abs(A[i][i]))
        beta[i] = soma
    if max(beta) < 1:
        return True
    return False

def calcularDeterminante(A):
    # calcula o determinante de uma matriz, de forma recursiva
    # utiliza o método de Laplace
    if len(A) == 2:
        determinante = A[0][0] * A[1][1] - A[0][1] * A[1][0]
        return determinante

    det = 0
    for coluna_atual in range(len(A)):
        sinal = (-1) ** coluna_atual
        submatriz = []
        for linha in A[1:]:
            sublinha = linha[:coluna_atual] + linha[coluna_atual + 1:]
            submatriz.append(sublinha)
        det += sinal * A[0][coluna_atual] * calcularDeterminante(submatriz)
    
    return det

def main():
    A = input("Digite a matriz de coeficientes, no formato [[a11, a12, ..., a1n], [a21, a22, ..., a2n], ..., [an1, an2, ..., ann]]: ")
    b = input("Digite o vetor de termos independentes, no formato [x1, x2, ..., xn] : ")
    tol = float(input("Digite a tolerância: "))
    maxIt = int(input("Digite o número máximo de iterações: "))

    A = eval(A)
    b = eval(b)

    if calcularDeterminante(A) == 0:
        print("O determinante da matriz de coeficientes é igual a zero. O sistema não tem solução única.")
        return

    conv = convergenciaLinhas(A) and convergenciaColunas(A)
    if conv:
        print("A matriz converge")
    else:
        print("A matriz não atende aos critérios de convergência por linhas e/ou colunas")

    convSassenfeld = criterioSassenfeld(A)
    if convSassenfeld:
        print("A matriz atende ao critério de Sassenfeld")
    else:
        print("A matriz não atende ao critério de Sassenfeld")

    x = seidel(A, b, tol, maxIt)
    print("x = ", x)
            

if __name__ == "__main__":
    """
    A = [[10, 2, 3], [1, 5, 1], [2, 3, 10]]
    b = [7, -8, 6]
    tol = 0.05
    maxIt = 100

    if calcularDeterminante(A) == 0:
        print("O determinante da matriz de coeficientes é igual a zero. O sistema não tem solução única.")
    else:
        conv = convergenciaLinhas(A) and convergenciaColunas(A)
        if conv:
            print("A matriz converge")
        else:
            print("A matriz não atende aos critérios de convergência")

        x = seidel(A, b, tol, maxIt)
        print("x = ", x)
    """

    main() # para escrever as matrizes e vetores pelo código, comente essa linha e descomente as linhas acima