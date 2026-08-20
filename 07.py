def calcular_raiz_quadrada():
    try:
        numero = float(input("Digite um número positivo: "))
    except ValueError:
        print("Entrada inválida. Digite um valor numérico.")
        return

    if numero < 0:
        print("Não é possível calcular a raiz real de um número negativo.")
        return
    if numero == 0:
        print("A raiz quadrada de 0 é: 0.0000")
        return

    # Método Babilônico / Newton-Raphson
    tolerancia = 1e-6  # Garante precisão acima de 4 casas decimais
    estimativa = numero / 2.0

    while True:
        proxima_estimativa = (estimativa + (numero / estimativa)) / 2.0
        # Condição de parada baseada na diferença entre iterações
        if abs(proxima_estimativa - estimativa) < tolerancia:
            break
        estimativa = proxima_estimativa

    print(f"Raiz quadrada calculada: {proxima_estimativa:.4f}")



calcular_raiz_quadrada()