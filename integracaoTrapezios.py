import math


def m_funcao(x, funcao=None) -> float:
    """
        Trasnforma a string na expressão matemática relacionada, devolvendo o valor da expressão.
        A função aceita a constante matemática e = 2.718281..., log10(x) (log de x na base 10) e ln(x) (logaritmo
        natural).

        Parâmetros:
            - x: valor da váriavel em que a expressão será calculada.
            - funcao: String a ser transformada.

        Retorna:
            - Valor da expressão relacionada a string funcao no ponto x.
    """

    if funcao is None:
        funcao = input()

    if funcao.__contains__("e"):
        funcao = funcao.replace("e", str(math.e))
    if funcao.__contains__("log(x)"):
        funcao = funcao.replace("log(x)", str(math.log10(x)))
    if funcao.__contains__("ln(x)"):
        funcao = funcao.replace("ln(x)", str(math.log(x)))
    if funcao.__contains__("cos(x)"):
        funcao = funcao.replace("cos(x)", str(math.cos(x)))
    if funcao.__contains__("sen(x)"):
        funcao = funcao.replace("sen(x)", str(math.sin(x)))

    # Calcular o valor da expressão no ponto x
    expressao = eval(funcao.replace("x", str(x)))
    return expressao


def integracao_trapezios(funcao, a, b, n) -> float:
    """
        Calcula a integral de uma função f(x) usando o método de integração dos Trapézios.

        Parâmetros:
            - funcao: Função a ser integrada.
            - a: Limite inferior do intervalo de integração.
            - b: Limite superior do intervalo de integração.
            - n: Número de subintervalos.

        Retorna:
            - Aproximação da integral da função f(x) no intervalo [a, b].
    """
    # Calcula o passo
    delta = (b - a) / n

    # Valor inicial
    x = a

    # Soma inicia em 0
    soma = 0

    # Faz a iteração n vezes
    for i in range(n - 1):
        # Calcula a soma nos próximos pontos
        soma += delta / 2 * (m_funcao(x, funcao) + m_funcao(x + delta, funcao))
        # Atualiza o x para a proxima iteração
        x += delta

    # Retorna o valor da integral
    return soma


if __name__ == "__main__":
    funcao = input("Entre com f(x): ")
    a = float(input("Limite inferior do intervalo: "))
    b = float(input("Limite superior do intervalo: "))
    n = int(input("Número de intervalos a serem usados: "))

    soma = integracao_trapezios(funcao, a, b, n)
    print(f"Resultado da integral: {soma}")
