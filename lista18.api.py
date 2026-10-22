from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/api")
async def questoes():
    return [
        {
            "pergunta": "Qual das seguintes estruturas de dados em Python e mutavel?",
            "alternativa1": "Tupla (tuple)",
            "alternativa2": "Lista (list)",
            "alternativa3": "String (str)",
            "alternativa4": "Inteiro (int)",
            "alternativa_correta": "alternativa2"
        }, {
            "pergunta": "Qual palavra-chave e utilizada para definir uma funcao em Python?",
            "alternativa1": "function",
            "alternativa2": "func",
            "alternativa3": "def",
            "alternativa4": "define",
            "alternativa_correta": "alternativa3"
        }, {
            "pergunta": "Qual e o resultado da expressao `type([])` no console Python?",
            "alternativa1": "<class 'list'>",
            "alternativa2": "<class 'array'>",
            "alternativa3": "<class 'dict'>",
            "alternativa4": "<class 'set'>",
            "alternativa_correta": "alternativa1"
        }, {
            "pergunta": "Qual operador e utilizado para exponenciacao (potencia) em Python?",
            "alternativa1": "^",
            "alternativa2": "**",
            "alternativa3": "^^",
            "alternativa4": "exp()",
            "alternativa_correta": "alternativa2"
        }, {
            "pergunta": "O que o metodo `.get()` de um dicionario faz quando a chave consultada nao existe?",
            "alternativa1": "Lanca uma excecao do tipo KeyError",
            "alternativa2": "Cria a chave automaticamente com valor vazio",
            "alternativa3": "Retorna None (ou o valor padrao definido) sem gerar erro",
            "alternativa4": "Trava a execucao do programa",
            "alternativa_correta": "alternativa3"
        }
    ]

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)