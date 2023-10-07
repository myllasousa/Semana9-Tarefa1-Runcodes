n1 = int(input(""))
n2 = int(input(""))
n3 = int(input(""))

v_difer1 = abs(n1 - n2)
v_difer2 = abs(n1 - n3)

def menor():
    if v_difer1 < v_difer2:
        return v_difer1
    else:
        return v_difer2

resultado = menor()
print(resultado)
