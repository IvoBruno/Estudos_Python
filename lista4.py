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

#q1_cadastro()
q2_lista_inversa()