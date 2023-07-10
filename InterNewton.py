def interpolacao_newton(x, dados):
    #Aqui vamos calcular a quantidade de dados para saber o grau do polinômio interpolador 
    n = len(dados) - 1  


    #Aqui estamos percorrendo a lista de pontos e criando uma nova lista apenas com os valores de 𝑥
    xs = [ponto[0] for ponto in dados]
    fs = [ponto[1] for ponto in dados]

    #Aqui estamos criando a matriz onde cada elemento da matriz representa uma diferença dividida
    tabela_dividida = [[0.0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        tabela_dividida[i][0] = fs[i]

    # Calcular as diferenças divididas
    for j in range(1, n + 1):
        for i in range(j, n + 1):
            tabela_dividida[i][j] = (tabela_dividida[i][j - 1] - tabela_dividida[i - 1][j - 1]) / (xs[i] - xs[i - j])

    # Agora vamos calcular o polinômio interpolador
    valor = fs[0]
    prod = 1.0

    for i in range(1, n + 1):
        prod *= (x - xs[i - 1])
        valor += tabela_dividida[i][i] * prod

    # calcular o erro estimado
    ErroEstimado = abs(valor - interpolador(x, xs, fs))

    return valor, ErroEstimado

def interpolador(x, xs, fs):
    # realiza a interpolação linear pra estimar f(x)
    for i in range(len(xs) - 1):
        if xs[i] <= x <= xs[i + 1]:
            slope = (fs[i + 1] - fs[i]) / (xs[i + 1] - xs[i])
            return fs[i] + slope * (x - xs[i])
    raise ValueError("x está fora do intervalo dos pontos de dados") 

# Exemplo para realização de um teste de funcionamento:

dados = [(0.0, 1.0), (1.0, 2.0), (3.0, 3.0), (4.0, 5.0)]
xi = 2.5

valor, ErroEstimado = interpolacao_newton(xi, dados)

print(f'O valor estimado de f({xi}) é: {valor}')
print(f'O valor do erro estimado é: {ErroEstimado}')
