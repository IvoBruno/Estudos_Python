import random

def q1_cadastro():
    cadastros: list[dict] = []
    while True:
        nome: str = input("Nome: ")
        idade: int = int(input("Idade: "))
        altura: float = float(input("Altura: "))
        estudante_input: str = input("É estudante? (S|N): ").strip().upper()
        estudante: bool = estudante_input == 'S'
        hobbie_input: str = input("Digite os hobbies, separando por virgula: ")
        hobbie: list[str] = hobbie_input.split(',')

        pessoa: dict = {
            "nome": nome,
            "idade": idade,
            "altura": altura,
            "estudante": estudante,
            "hobbie": hobbie
        }
        cadastros.append(pessoa)
        novo_cad: str = input("Deseja cadastrar mais alguém? (S|N):").strip().upper()
        if (novo_cad == "N"): 
            break
    print("===Cadastros===")
    for cad in cadastros:
        print(cad)

def q2_lista_inversa():
    lista: list[int] = []
    for _ in range(10):
        num_rand = random.randint(0, 20)
        lista.append(num_rand)
    print("Lista original: ")
    print(lista)
    lista_inversa = lista[::-1]
    print("Lista invertida: ")
    print(lista_inversa)

def q3_maior_par():
    lista: list[int] = []
    for _ in range(30):
        num_rand = random.randint(-100,100)
        lista.append(num_rand)
    print(lista)
    maior_par: int= lista[0]
    for num in lista:
        if (num%2 == 0 and (num > maior_par or maior_par%2 != 0)):
            maior_par = num
    if(maior_par%2 != 0):
        print("Nenhum valor par encontrado")
    else:
        print(f"O maior par é [{maior_par}]")

def q4_maior_menor_pares():
    lista: list[int] = []
    for _ in range(10):
        num_rand = random.randint(0,30)
        lista.append(num_rand)
    print(lista)
    maior_par = lista[0]
    menor_par = lista[0]
    for num in lista:
        if(num%2 ==0):
            if(num > maior_par or maior_par%2!= 0): maior_par = num
            if(num < menor_par or menor_par%2!= 0): menor_par = num
    if(maior_par%2!=0):
        print("Nenhum valor par encontrado")
        return
    print(maior_par, " - ", menor_par)
    for i in range(maior_par, menor_par - 1, -2):
        print(i)

#q1_cadastro()
#q2_lista_inversa()
#q3_maior_par()
#q4_maior_menor_pares()