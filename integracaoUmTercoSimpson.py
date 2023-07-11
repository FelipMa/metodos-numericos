import math


def m_funcao(x, funcao=None) -> float:
    """
        Trasnforma a string na expressão matemática relacionada, devolvendo o valor da expressão.
        A função aceita a constante matemática e = 2.718281..., pi, log10(x) (log de x na base 10), ln(x) (logaritmo
        natural), cos(s) e sen(x).

        Parâmetros:
            - x: valor da váriavel em que a expressão será calculada.
            - funcao: String a ser transformada.

        Retorna:
            - Valor da expressão relacionada a string funcao no ponto x.
    """

    if funcao is None:
        funcao = input()

    # OBS: o método só é capaz de fazer a troca pelas funções da forma apresentada abaixo, o que significa que não
    # funcionam através de uma composição delas. Por exemplo:
    #  String aceita: 3*x**2 - 5x - 10
    #  String não aceito: cos(x**2)
    if funcao.__contains__("pi"):
        funcao = funcao.replace("pi", str(math.pi))
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
    integral = eval(funcao.replace("x", str(x)))
    return integral


def integracao_1_3_simpson(funcao, a, b, n):
    """
        Calcula a integral de uma função f(x) usando o método de integração 1/3 de Simpson. Para o funcionamento da
        função, o número de subintervalos deve ser par.

        Parâmetros:
        - funcao (string): Função a ser integrada.
        - a (float): Limite inferior do intervalo de integração.
        - b (float): Limite superior do intervalo de integração.
        - n (int): Número de subintervalos (deve ser par).

        Retorna:
        - Aproximação da integral da função f(x) no intervalo [a, b].
    """

    # Verifica se o número de subintervalo é par. Caso não, será lançado um erro
    if n % 2 != 0:
        raise ValueError("O número de subintervalos deve ser par.")

    # Calcula o passo
    h = (b - a) / n

    # Valor inicial
    x = a

    integral = m_funcao(a, funcao) + m_funcao(b, funcao)

    # Faz a iteração n vezes
    for i in range(1, n):
        # Atualiza o passo
        x += h

        # Verifica se a iteração é par ou impar para a soma na integral
        if i % 2 == 0:
            integral += 2 * m_funcao(x, funcao)
        else:
            integral += 4 * m_funcao(x, funcao)

    # Multiplica pelo valor
    integral *= h / 3

    # Retorna o valor da integral
    return integral


if __name__ == "__main__":
    # Programa para usar os métodos:
    # funcao = input("Entre com f(x): ")
    # a = float(input("Limite inferior do intervalo: "))
    # b = float(input("Limite superior do intervalo: "))
    # n = int(input("Número de intervalos a serem usados: "))
    #
    # soma = integracao_trapezios(funcao, a, b, n)
    # print(f"Resultado da integral: {soma}")

    # Exemplo de utilização:
    print("Exemplo de utilização: ")
    f = "3*x**2 - 5x - 10 + cos(x**2)"
    a = 5
    b = 10
    n = 10000
    print(f" função: {f};\n a: {a};\n b: {b};\n n: {n}")
    resultado = integracao_1_3_simpson(f, a, b, n)

    print(f"'Valor da integral': {resultado}")
