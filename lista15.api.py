from fastapi import FastAPI, HTTPException, status
from typing import Optional
import uvicorn

class Tarefa():
    def __init__(self, id: int, titulo: str, prioridade: str = "BAIXA"):
        self.id = id
        self.titulo = titulo
        self.prioridade = prioridade.upper()

app = FastAPI(
    title="Lista de Tarefas",
    description="API para gerenciar uma lista de tarefas",
    version="1.0.0"
)

def inicia_fastapi():
    uvicorn.run(app, host="127.0.0.1", port=8000)

tarefas = [
    Tarefa(id=1, titulo="Comprar leite", prioridade="alta"),
    Tarefa(id=2, titulo="Estudar FastAPI", prioridade="media"),
    Tarefa(id=3, titulo="Fazer exercícios", prioridade="baixa")
]

@app.get("/")
async def root():
    return {"message": "Bem-vindo à API de Lista de Tarefas!"}

@app.get("/tarefas")
async def listar_tarefas():
    return {"tarefas": tarefas}

@app.get("/tarefas/{id}")
async def obter_tarefa(id: int):
    for tarefa in tarefas:
        if tarefa.id == id:
            return {"tarefa": tarefa}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada")

@app.get("/tarefas/prioridade/{prioridade}")
async def listar_tarefas_por_prioridade(prioridade: str):
    prioridade = prioridade.upper()
    tarefas_filtradas = [tarefa for tarefa in tarefas if tarefa.prioridade == prioridade]
    if not tarefas_filtradas:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhuma tarefa encontrada com a prioridade especificada")
    return {"tarefas": tarefas_filtradas}

@app.post("/tarefas", status_code=status.HTTP_201_CREATED)
async def criar_tarefa(titulo: str, prioridade: Optional[str] = "BAIXA"):
    id_novo = max(tarefa.id for tarefa in tarefas) + 1 if tarefas else 1
    nova_tarefa = Tarefa(id=id_novo, titulo=titulo, prioridade=prioridade)
    tarefas.append(nova_tarefa)
    return {"tarefa": nova_tarefa}

@app.put("/tarefas/{id}", status_code=status.HTTP_200_OK)
async def atualizar_tarefa(id: int, titulo: Optional[str] = None, prioridade: Optional[str] = None):
    for tarefa in tarefas:
        if tarefa.id == id:
            if titulo:
                tarefa.titulo = titulo
            if prioridade:
                tarefa.prioridade = prioridade.upper()
            return {"tarefa": tarefa}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada")

@app.delete("/tarefas/{id}")
async def deletar_tarefa(id: int):
    for tarefa in tarefas:
        if tarefa.id == id:
            tarefas.remove(tarefa)
            return {"message": "Tarefa deletada com sucesso"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
