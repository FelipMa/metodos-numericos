def interpolacao_newton(x, dados):
    #Aqui vamos calcular a quantidade de dados para saber o grau do polinômio interpolador 
    n = len(dados) - 1
    print(f'Grau do polinômio interpolador: {n}')

    #Aqui estamos percorrendo a lista de pontos e criando novas listas com os valores de x e y
    xs = [ponto[0] for ponto in dados]
    ys = [ponto[1] for ponto in dados]

    #Aqui estamos criando a matriz onde cada elemento da matriz representa uma diferença dividida
    tabela_dividida = [[0.0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        tabela_dividida[i][0] = ys[i]
    #Por enquanto, temos a tabela com apenas os valores de x e y

    # Calcular as diferenças divididas
    for j in range(1, n + 1): # j = ordem da diferença dividida
        for i in range(j, n + 1): # loop para calcular as diferenças divididas de ordem j
            tabela_dividida[i][j] = (tabela_dividida[i][j - 1] - tabela_dividida[i - 1][j - 1]) / (xs[i] - xs[i - j])
    #Ao final, temos a tabela com os valores de x, y e as diferenças divididas para cada ordem

    # Agora vamos calcular o polinômio interpolador
    valor = ys[0] # valor = somatório (começa em y0)
    prod = 1.0 # prod = produtório

    for i in range(1, n + 1):
        prod *= (x - xs[i - 1])
        valor += tabela_dividida[i][i] * prod

    #Aqui vamos calcular o erro estimado
    erroEstimado = 1 # começa 1 pois vamos realizar um produto

    #Aqui vamos pegar o maior valor absoluto da tabela de diferenças divididas
    max = 0
    for j in range(1, n + 1): 
        for i in range(j, n + 1):
            if abs(tabela_dividida[i][j]) > max:
                max = abs(tabela_dividida[i][j])
    
    for i in range(0, n + 1):
        erroEstimado *= (x - xs[i]) # multiplicamos os valores de x - x0, x - x1, x - x2, ..., x - xn
    
    erroEstimado = abs(erroEstimado) # pegamos o valor absoluto do produto acima

    erroEstimado = erroEstimado * max # multiplicamos o produto acima pelo maior valor absoluto da tabela de diferenças divididas

    return valor, erroEstimado


# Exemplo para realização de um teste de funcionamento:

dados = [(0, 0), (1, 1), (2, 4), (3, 9)]
xi = 1.5

valor, erroEstimado = interpolacao_newton(xi, dados)

print(f'O valor estimado de f({xi}) é: {valor}')
print(f'O valor do erro estimado é: {erroEstimado}')
