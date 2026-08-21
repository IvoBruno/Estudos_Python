def q1_maior_nota():
    maior_nota = []
    alunos = []
    try:
        qnt_alunos = int(input("Digite a quatidade de alunos: "))
    except ValueError:
        print("Valor inválido, deve ser um número inteiro.")
        return
    for i in range(qnt_alunos):
        nome = input("Digite o nome do aluno: ")
        try:
            nota = int(input("Digite a nota do aluno: "))
        except ValueError:
            print("Valor inválido, deve ser um numero inteiro.")
            continue
        alunos.append({"nome":nome, "nota": nota})

    for aluno in alunos:
        if(len(maior_nota) == 0):
            maior_nota.append(aluno)
        elif(aluno["nota"] > maior_nota[0]["nota"]):
            maior_nota.clear()
            maior_nota.append(aluno)
        elif(aluno["nota"] == maior_nota[0]["nota"]): 
            maior_nota.append(aluno)
    print(f"Maior(res) nota(s): {maior_nota}")

def q2_substitui_banana_maca():
    original = input("Digite o texto a ser alterado: ")
    processado = original.replace("banana","maçã")
    print(processado)
    
def q3_substitui_vogais():
    texto = input("Digite o texto a ser adaptado: ")
    vogais = "aeiouAEIOU"
    for v in vogais:
        texto = texto.replace(v, "a")
    print("Texto adaptado: ", texto)

def q4_inverte_nome():
    nome = input("Digite seu nome: ")
    print(nome[::-1])

def q5_conta_letra ():
    texto = input("Digite o texto a ser verificado: ")
    letra = input("Digite a letra a ser buscada: ")
    cont = texto.count(letra)
    print(f"A letra [{letra}] aparece [{cont}] vez(es).")

# q1_maior_nota()
# q2_substitui_banana_maca()
# q3_substitui_vogais()
# q4_inverte_nome()
# q5_conta_letra()