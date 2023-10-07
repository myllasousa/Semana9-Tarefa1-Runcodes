def calculo(valor1, valor2, operacao):
    if operador == 1:
        return n1 + n2
    elif operador == 2:
        return n1 - n2
    elif operador == 3:
        return n1 * n2
    else:
        return n1 / n2

n1 = int(input(""))
n2 = int(input(""))
operador = int(input(""))
resultado = calculo(n1, n2, operador)
print(round(resultado,2))