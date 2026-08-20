value = -1
while(value != 0):
    try:
        value = int(input("Digite o valor para calcular ou '0' para sair:"))
    except ValueError:
        print("Valor deve ser um número inteiro")
        continue
    if (value == 0): break
    for i in range(1,11):
        print(f"{value} * {i:02d} = {value*i}")