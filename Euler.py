def euler(f_y_linha, x0, y0, h, n):

    xn = x0 + n*h

    print("\nIterações:")
    for i in range(n):
        ylinha = f_y_linha(x0, y0)
        yn = y0 + h * ylinha
        print(f"| Iteração {i} | x = {x0} | y = {y0} | y' = {ylinha} | y+1 = {yn} |")
        print("---------------------------------------------------------")
        y0 = yn
        x0 = x0+h
    
    print("Resultado:")
    print(f"Em x={xn}, y={yn}")

if __name__ == "__main__":
    def f_y_linha(x,y): # dy/dx = f(x,y)
        f = 2*x # troque aqui a função!
        return f
    
    x0 = 2 # x inicial
    y0 = 4 # y inicial
    h = 0.5 # tamanho do passo
    n = 2 # número de subintervalos

    euler(f_y_linha, x0, y0, h, n)
    