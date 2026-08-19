def checaPrimo(num):
    check = True
    print(int(num/2))
    for i in range(2, int(num/2)+2):
        print("Comparando com ", i, "...")
        if (num % i == 0):
            check = False
            break
    return check

valorChecado = int(input("Digite um número inteiro positivo: "))
if(valorChecado < 0):
    print("Valor inválido!")
else:
    print("[", valorChecado, "] é primo?", checaPrimo(valorChecado))