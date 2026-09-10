def tem_lower(valor: str):
    for i in valor:
        if(i.islower()): return True
    return False


def q1_numeros_repetidos():
    lista: list[int] = [1, 2, 3, 5, 4, 5, 1, 9, 3, 9]
    mapa = {}
    for i in lista:
        if i in mapa.keys():
            mapa[i] += 1
        else:
            mapa[i] = 1
    repetidos= []
    for key, value in mapa.items():
        if (value > 1):
            repetidos.append(key)
    print(repetidos)

def q2_upper_strings():
    lista = ["ifpi", "UFDPar", "UESPI", "usp", "UEMA"]
    maiusculos = []
    for i in lista:
        if (not tem_lower(i) and len(i)>4): maiusculos.append(i)
    print(maiusculos)

def q3_soma_tupla():
    soma = 0;
    tuplas = ((1,2), (3,4), (5,6))
    for tupla in tuplas:
        soma += tupla[1]
    print(f"Soma dos segundos valores das tuplas: {soma}")

def q4_tupla_lista():
    tuplas = ((1,2), (3,4), (5,6))
    listas = []
    for tupla in tuplas:
        listas.append([tupla[0], tupla[1]+10])
    print(listas)

def q5_arvore():
    target: int = int(input("Digite o valor alvo: "))
    lista = [1]
    while(len(lista) < target):
        print(lista)
        lista.append(lista[-1]+1)
    while(len(lista) > 0):
        print(lista)
        lista.pop()


#q1_numeros_repetidos()
#q2_upper_strings()
#q3_soma_tupla()
#q4_tupla_lista()
q5_arvore()