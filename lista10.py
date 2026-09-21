def q1_frequencia_palavras(frase: str = "o rato roeu a roupa do rei de roma o rato"):
    contagem = {}
    for palavra in frase.lower().split():
        contagem[palavra] = contagem.get(palavra, 0) + 1
    print(f"Frequência: {contagem}")
    return contagem


def q2_media_alunos(alunos: dict[str, list[float]] = None):
    if alunos is None:
        alunos = {"Ana": [8.0, 7.5, 9.0], "Bruno": [6.0, 5.5, 7.0], "Carla": [9.5, 10.0, 9.0]}
    medias = {nome: round(sum(notas) / len(notas), 2) for nome, notas in alunos.items()}
    print(f"Médias: {medias}")
    return medias


def q3_carrinho_compras(itens: list[tuple[str, int]] = None):
    if itens is None:
        itens = [("Maçã", 3), ("Pão", 2), ("Leite", 1), ("Maçã", 2)]
    carrinho = {}
    for produto, quantidade in itens:
        carrinho[produto] = carrinho.get(produto, 0) + quantidade
    print(f"Carrinho: {carrinho}")
    return carrinho


def q4_contagem_convidados(convidados: list[str] = None):
    if convidados is None:
        convidados = ["Ana", "Carlos", "Ana", "Beatriz", "Carlos", "Ana"]
    contagem = {}
    for nome in convidados:
        contagem[nome] = contagem.get(nome, 0) + 1
    print(f"Convidados: {contagem}")
    return contagem


def q5_signo(dia: int = 15, mes: int = 8, ano: int = 1995):
    signos = {
        1: (20, "Capricórnio", "Aquário"),
        2: (19, "Aquário", "Peixes"),
        3: (21, "Peixes", "Áries"),
        4: (20, "Áries", "Touro"),
        5: (21, "Touro", "Gêmeos"),
        6: (21, "Gêmeos", "Câncer"),
        7: (23, "Câncer", "Leão"),
        8: (23, "Leão", "Virgem"),
        9: (23, "Virgem", "Libra"),
        10: (23, "Libra", "Escorpião"),
        11: (22, "Escorpião", "Sagitário"),
        12: (22, "Sagitário", "Capricórnio"),
    }
    corte, antes, depois = signos[mes]
    signo = antes if dia < corte else depois
    print(f"Data: {dia:02d}/{mes:02d}/{ano} -> Signo: {signo}")
    return signo


if __name__ == "__main__":
    q1_frequencia_palavras()
    #q2_media_alunos()
    #q3_carrinho_compras()
    #q4_contagem_convidados()
    #q5_signo()

