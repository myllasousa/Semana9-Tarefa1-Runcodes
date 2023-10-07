n1 = int(input(""))
n2 = int(input(""))
n3 = int(input(""))

def iguais_dife():
    if n1 == n2 and n2 == n3 and n1 == n3:
        print("Todos os valores são iguais")
    elif n1 != n2 and n2 != n3 and n1 != n3:
        print("Todos os valores são diferentes")
    else:
        print("Existem dois valores iguais e um diferente")

iguais_dife()