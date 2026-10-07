import streamlit as st
import requests

api_url = "http://127.0.0.1:8000"

st.set_page_config("Lista de Tarefas", page_icon=":clipboard:", layout="centered")
st.title(":clipboard: Lista de Tarefas")

try:
    response = requests.get(f"{api_url}/tarefas")
    if response.status_code == 200:
        tarefas = response.json().get("tarefas", [])
        if tarefas:
            for tarefa in tarefas:
                st.write(f"- **[{tarefa['id']:02d}] {tarefa['titulo']}** [Prioridade: `{tarefa['prioridade']}`]")
        else:
            st.info("Nenhuma tarefa cadastrada.")
    else:
        st.error("Erro ao carregar tarefas da API.")
except requests.exceptions.RequestException:
    st.warning("Não foi possível conectar à API. Verifique se `lista15.api.py` está rodando em http://127.0.0.1:8000")

with st.sidebar:
    st.header("Adicionar Tarefa")
    titulo = st.text_input("Título da Tarefa")
    prioridade = st.selectbox("Prioridade", ["BAIXA", "MÉDIA", "ALTA"])
    if st.button("Adicionar"):
        if titulo.strip():
            response = requests.post(f"{api_url}/tarefas", params={"titulo": titulo, "prioridade": prioridade})
            if response.status_code == 201:
                st.success("Tarefa adicionada com sucesso!")
                st.rerun()
            else:
                st.error("Erro ao adicionar tarefa.")
        else:
            st.warning("Informe um título para a tarefa.")
    st.header("Filtrar Tarefas por Prioridade")
    prioridade_filtro = st.selectbox("Prioridade", ["TODAS", "BAIXA", "MÉDIA", "ALTA"])
    if st.button("Filtrar"):
        if prioridade_filtro == "TODAS":
            st.rerun()
        else:
            response = requests.get(f"{api_url}/tarefas/prioridade/{prioridade_filtro}")
            if response.status_code == 200:
                tarefas_filtradas = response.json().get("tarefas", [])
                if tarefas_filtradas:
                    st.write(f"Tarefas com prioridade `{prioridade_filtro}`:")
                    for tarefa in tarefas_filtradas:
                        st.write(f"- **[{tarefa['id']:02d}] {tarefa['titulo']}**")
                else:
                    st.info(f"Nenhuma tarefa encontrada com prioridade `{prioridade_filtro}`.")
            else:
                st.error("Erro ao filtrar tarefas.")
    st.header("Atualizar Tarefa")
    id_tarefa = st.number_input("ID da Tarefa", min_value=1, step=1)
    novo_titulo = st.text_input("Novo Título (opcional)")
    nova_prioridade = st.selectbox("Nova Prioridade (opcional)", ["", "BAIXA", "MÉDIA", "ALTA"])
    if st.button("Atualizar"):
        if id_tarefa:
            params = {}
            if novo_titulo.strip():
                params["titulo"] = novo_titulo
            if nova_prioridade:
                params["prioridade"] = nova_prioridade
            response = requests.put(f"{api_url}/tarefas/{id_tarefa}", params=params)
            if response.status_code == 200:
                st.success("Tarefa atualizada com sucesso!")
                st.rerun()
            elif response.status_code == 404:
                st.error("Tarefa não encontrada.")
            else:
                st.error("Erro ao atualizar tarefa.")
        else:
            st.warning("Informe o ID da tarefa para atualizar.")
    st.header("Deletar Tarefa")
    id_tarefa_deletar = st.number_input("ID da Tarefa para Deletar", min_value=1, step=1, key="deletar")
    if st.button("Deletar"):
        if id_tarefa_deletar:
            response = requests.delete(f"{api_url}/tarefas/{id_tarefa_deletar}")
            if response.status_code == 200:
                st.success("Tarefa deletada com sucesso!")
                st.rerun()
            elif response.status_code == 404:
                st.error("Tarefa não encontrada.")
            else:
                st.error("Erro ao deletar tarefa.")
        else:
            st.warning("Informe o ID da tarefa para deletar.")
