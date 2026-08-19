def perfectNumber(number):
    divisores = []
    for i in range(1, number):
        if (number % i == 0): divisores.append(i)
    for i in divisores:
        number -= i
    return number == 0

value = int(input("Digite um numero inteiro positivo: "))
if(value > 0):
    print(value, "é perfeito? ", perfectNumber(value))
else:
    print("Valor inválido")