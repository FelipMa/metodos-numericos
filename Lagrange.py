def lagrange(xi: float, xy: list): # xi = ponto a ser interpolado, xy = lista de pontos, cada ponto é uma tupla (x, y)
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

def main():
    print("Insira os pontos a serem interpolados no formato x0 y0 x1 y1 xn yn, separados apenas por espaço:")
    # exemplo: 1 1 2 4 3 9 4 16
    xy = input().split()
    for i in range(len(xy)): # transforma os pontos em float
        xy[i] = float(xy[i])

    xy = list(zip(xy[::2], xy[1::2])) # transforma a lista de pontos em uma lista de tuplas (x, y)

    print("Os pontos inseridos foram:", xy) # mostra os pontos inseridos
    xi = float(input("insira o ponto a ser interpolado: ")) # xi = ponto a ser interpolado

    print(f"O resultado da interpolação de Lagrange para os pontos escolhidos é: {lagrange(xi, xy)}") # mostra o resultado da interpolação de Lagrange

if __name__ == "__main__":
    """
    xy = [(1, 1), (2, 4), (3, 9), (4, 16)]
    xi = 2.5
    print(lagrange(xi, xy))
    """

    main() # para escrever as variáveis em código, comente essa linha e descomente as linhas acima