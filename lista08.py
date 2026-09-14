import csv
import json

def adiciona_item_json(item):
    with open("produtos.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
    dados.append(item)
    with open("produtos.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)

def remove_item_json(id):
    with open("produtos.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
    dados_atualizados = [item for item in dados if item['id'] != id]
    with open("produtos.json", "w", encoding="utf-8") as f:
        json.dump(dados_atualizados, f, indent=2, ensure_ascii=False)
    
def q1_total_produtos():
    with open("produtos.csv", "r", encoding="utf-8", newline="") as f:
        leitor = csv.DictReader(f, delimiter=",")
        for linha in leitor:
            valor_total += float(linha['preco'])
    print(f'Valor total: R${valor_total:.2f}')

def q2_loja_json():
    with open("produtos.json", "r", encoding="utf-8") as f:
        produtos = json.load(f)

    print(f'{"Lista original":=^50}')
    for item in produtos:
        print(f'{item['nome']:>35} | R${item['preco']:.2f}')
    
    adiciona_item_json({"id": 11, "nome": "Lampada Smart", "preco": 45.99, "quantidade_estoque": 20})
    with open("produtos.json", "r", encoding="utf-8") as f:
        produtos = json.load(f)
    print(f'{"Lampara smart adicionada":=^50}')
    for item in produtos:
        print(f'{item['nome']:>35} | R${item['preco']:.2f}')
        
    remove_item_json(9)
    with open("produtos.json", "r", encoding="utf-8") as f:
        produtos = json.load(f)
    print(f'{"Id 9 removido":=^50}')
    for item in produtos:
        print(f'{item['nome']:>35} | R${item['preco']:.2f}')
    
#q1_total_produtos()
q2_loja_json()
