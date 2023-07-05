"""
Divisão:
- Sistemas lineares Gauss Jacobi
- Sistemas lineares Gauss Seidel
- Interpolação Lagrange
- Interpolação Newton
- Integração
"""

print("hello wolrd")

def lagrange(xi: float, xy: list): # xi = ponto a ser interpolado, xy = lista de pontos
    yi = 0 # yi = ponto interpolado, começa em 0, pois é um somatório
    xlist = [] # xlist = lista de x's
    ylist = [] # ylist = lista de y's
    for i in range(len(xy)): # separa os x's e y's em listas diferentes
        xlist.append(xy[i][0])
        ylist.append(xy[i][1])
    
    for k in range(len(xy)):
        Lk = 1 # Lk = operador Lk(x), começa em 1, pois é um produtório
        for j in range(len(xy)):
            if k != j:
                Lk = Lk * (xi - xlist[j]) / (xlist[k] - xlist[j]) # Lk é o produtório de (xi - xj)/(xk - xj) para j != k
        yi = yi + Lk * ylist[k] # o ponto interpolado (yi) é o somatório de Lk * yk

    return yi

print("teste de lagrange para os pontos (0,0), (1,1), (2,4), (3,9), (4,16) interpolando em 2.5")
teste = lagrange(2.5, [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16]])
print(f"resultado: {teste}")