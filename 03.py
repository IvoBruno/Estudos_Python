def somaQuadados(value):
    acumulador = 0
    for i in value:
        print(i,"² = ", int(i)**2)
        acumulador += int(i)**2
    return acumulador

valor = input("Digite um número: ")
print("A soma dos quadrados dos dígitos é:", somaQuadados(valor))
