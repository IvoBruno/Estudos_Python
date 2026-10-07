import requests

def consulta_cotacao():
    url = "https://economia.awesomeapi.com.br/json/last/usd-brl,usd-eur,btc-usd,btc-brl"
    moedas = ["USDBRL", "USDEUR", "BTCUSD", "BTCBRL"]
    selecao = int(input("=====COTACAO=====\n1 - BRL->USD\n2 - EUR->USD\n3 - BTC->USD\n4 - BTC->EUR\n"))
    selecionada = moedas[selecao - 1] if 0 < selecao <= len(moedas) else "inválido"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        if selecionada in dados:
            moeda = dados[selecionada]
            print(f"Moeda: {moeda['name']}")
            print(f"Compra: ${float(moeda['bid']):_.2f}")
            print(f"Venda: ${float(moeda['ask']):_.2f}")
        else:
            print("moeda nao localizada")
    except requests.exceptions.HTTPError as http_err:
        print(f"Erro HTTP encontrado: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Erro na requisicao: {err}")

if __name__ == "__main__":
    consulta_cotacao()