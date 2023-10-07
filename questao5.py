n = int(input(""))
def calculo():
    return n % 5

resultado = calculo()

def res_calculo():
    if resultado == 0:
        return (9 * n) + 7
    elif resultado == 1:
        if n % 2 == 0:
            return "par"
        else:
            return "ímpar"
    elif resultado == 2:
        return 5 * (n ** 2) - (3 * n) + 42
    elif resultado == 3:
        return n // 10
    elif resultado == 4:
        return n ** 2
    else:
        pass

resultado2 = res_calculo()
print(resultado2)
