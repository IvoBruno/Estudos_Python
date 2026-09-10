def q1_calcula_media(notas):
    if (len(notas) != 3):
        print("A lista de notas deve conter exatamente 3 elementos.")
        return None
    media = sum(notas) / len(notas)
    print(f"A média das notas é: {media}")

def q2_conta_pares():
    valor: int = int(input("Digite um valor inteiro: "))
    pares = 0
    for i in range(0, valor + 1):
        if (i % 2 == 0):
            pares += 1
    print(f"Quantidade de números pares entre 0 e {valor}: {pares}")

def q3_soma_multiplos():
    valor: int = int(input("Digite um valor inteiro: "))
    multiplos = 0
    for i in range(1, valor + 1):
        if (i % 3 == 0 or i % 5 == 0):
            multiplos += i
    print(f"Soma dos múltiplos de 3 e 5 entre 1 e {valor}: {multiplos}")

def q4_calculadora(num1, num2, operacao):
    if (operacao == 'soma'):
        resultado = num1 + num2
    elif (operacao == 'subtracao'):
        resultado = num1 - num2
    elif (operacao == 'multiplicacao'):
        resultado = num1 * num2
    elif (operacao == 'divisao'):
        if (num2 != 0):
            resultado = num1 / num2
        else:
            print("Erro: Divisão por zero.")
            return None
    else:
        print("Operação inválida.")
        return None
    print(f"Resultado da operação {num1} {operacao} {num2} = {resultado}")

def q5_estatisticas(*args):
    if len(args) == 0:
        print("Nenhum valor fornecido.")
        return None
    estatisticas = {}
    estatisticas['media'] = sum(args) / len(args)
    estatisticas['minimo'] = min(args)
    estatisticas['maximo'] = max(args)
    estatisticas['soma'] = sum(args)
    print(f"Estatísticas: {estatisticas}")

#q1_calcula_media([7.5, 8.0, 9.0])
#q2_conta_pares()
#q3_soma_multiplos()
#q4_calculadora(10, 0, "soma")
#q5_estatisticas(1, 2, 3, 4, 5)