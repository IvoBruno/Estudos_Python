def checaPrimo(num):
    check = True
    for i in range(2, int(num/2)+2):
        if (num % i == 0):
            check = False
            break
    return check

contPrimos = 0
numerosTestados = 1
while (contPrimos < 10):
    if (checaPrimo(numerosTestados)):
        print(numerosTestados, "é primo")
        contPrimos += 1
    numerosTestados += 1