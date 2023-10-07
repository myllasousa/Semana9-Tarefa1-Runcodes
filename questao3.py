def quadrado_retangulo(base, altura):
    if base == altura:
         print("QUADRADO")
    else:
        print(perimetro, area, sep = ' - ')


b = int(input(""))
a = int(input(""))
perimetro = 2 * (b + a)
area = b * a
quadrado_retangulo(a, b)