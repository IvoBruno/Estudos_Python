import json

def q1_alunos_medias():
    json_alunos = """
    [
        { "nome": "Ana", "idade": 20, "curso": "ADS", "notas": [8.0, 7.5, 9.0] },
        { "nome": "Carlos", "idade": 22, "curso": "ADS", "notas": [6.0, 6.5, 6.0] },
        { "nome": "Mariana", "idade": 21, "curso": "ADS", "notas": [9.0, 9.5, 9.0] },
        { "nome": "Pedro", "idade": 23, "curso": "ADS", "notas": [7.0, 7.5, 7.0] }
    ]
    """
    alunos = json.loads(json_alunos)
    max_aluno = alunos[0]
    print("===Médias dos alunos===")
    for aluno in alunos:
        aluno['media'] = sum(aluno['notas']) / len(aluno['notas'])
        print(f"{aluno['nome']} - média: {aluno['media']:.2f}")
        if aluno['media'] > max_aluno['media']: max_aluno = aluno

    print("\n===Alunos aprovados===")
    for aluno in alunos:
        if aluno['media'] >= 7: print(aluno['nome'])

    print(f"\n===Aluno com maior media===\n{max_aluno['nome']}| média: {max_aluno['media']:.2f}")

def q2_loja():
    json_loja = """
        {
  "loja": "TechStore",
  "produtos": [
    { "id": 1, "nome": "Teclado", "categoria": "Periféricos", "preco": 120.00, "estoque": 15 },
    { "id": 2, "nome": "Mouse", "categoria": "Periféricos", "preco": 80.00, "estoque": 5 },
    { "id": 3, "nome": "Monitor 24 Pol", "categoria": "Monitores", "preco": 850.00, "estoque": 8 },
    { "id": 4, "nome": "Headset Gamer", "categoria": "Áudio", "preco": 230.50, "estoque": 12 },
    { "id": 5, "nome": "Webcam 1080p", "categoria": "Periféricos", "preco": 190.00, "estoque": 20 },
    { "id": 6, "nome": "Mousepad Grande", "categoria": "Acessórios", "preco": 45.90, "estoque": 35 },
    { "id": 7, "nome": "SSD NVMe 1TB", "categoria": "Armazenamento", "preco": 420.00, "estoque": 10 },
    { "id": 8, "nome": "Cabo HDMI 2.0", "categoria": "Cabos", "preco": 25.00, "estoque": 50 },
    { "id": 9, "nome": "Memória RAM 16GB", "categoria": "Hardware", "preco": 310.00, "estoque": 14 },
    { "id": 10, "nome": "Suporte Articulado", "categoria": "Acessórios", "preco": 175.00, "estoque": 6 }
  ]
}
    """
    loja = json.loads(json_loja)
    print(f'{"Produtos":=^50}')
    for prod in loja['produtos']:
        print(prod['nome'])
    print(f'\n{"Estoque baixo":=^50}')
    for prod in loja['produtos']:
        if prod['estoque'] < 6: print(f"{prod['nome']:>18} | Estoque: {prod['estoque']}")
    print(f'\n{"Valor armazenado":=^50}')
    print("      NOME PRODUTO | VALOR UNIT | ESTOQUE | VALOR TOTAL")
    total_estoque = 0.0
    maior_valor_estoque = loja['produtos'][0]
    for prod in loja['produtos']:
        prod['valor_estoque'] = prod['preco'] * prod['estoque']
        total_estoque += prod['valor_estoque']
        if prod['valor_estoque'] > maior_valor_estoque['valor_estoque']:maior_valor_estoque = prod
        print(f"{prod['nome']:>18} | {prod['preco']:>10.2f} | {prod['estoque']:>7} | {prod['valor_estoque']:>10.2f}")
    print(f'\n{"Valor total em estoque":=^50}\nR${total_estoque:.2f}')
    print(f'\n{"Item com maior valor em estoque":=^50}\n{maior_valor_estoque['nome']} | R${maior_valor_estoque['valor_estoque']:.2f}')
    categoria = input("\nDigite a categoria que deseja buscar: ")
    print(f'{categoria.upper():=^50}')
    print("      NOME PRODUTO | VALOR UNIT | ESTOQUE | VALOR TOTAL")
    for prod in loja['produtos']:
        if prod['categoria'].upper() == categoria.upper():
            print(f"{prod['nome']:>18} | {prod['preco']:>10.2f} | {prod['estoque']:>7} | {prod['valor_estoque']:>10.2f}")

#q1_alunos_medias()
#q2_loja()