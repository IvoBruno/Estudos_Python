import json
import random
import streamlit as st

class Aluno():
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

if "alunos" not in st.session_state:
    st.session_state.alunos = [
        {"id": 1, "nome": "Alice"},
        {"id": 2, "nome": "Bob"},
        {"id": 3, "nome": "Charlie"},
        {"id": 4, "nome": "David"},
        {"id": 5, "nome": "Eva"},
    ]

st.set_page_config("Sorteio de Alunos", page_icon=":mortar_board:", layout="centered")
st.title(":mortar_board: Sorteio de Alunos")
novo_aluno = st.text_input("Digite o nome do novo aluno")
if st.button("Adicionar Aluno"):
    if novo_aluno.strip():
        novo_id = max(aluno["id"] for aluno in st.session_state.alunos) + 1
        st.session_state.alunos.append({"id": novo_id, "nome": novo_aluno.strip()})
        st.success(f"Aluno '{novo_aluno.strip()}' adicionado com sucesso!")
        st.rerun()
    else:
        st.warning("Informe o nome do aluno.")
st.markdown("\n".join([f"- **[{aluno['id']:02d}] {aluno['nome']}**" for aluno in st.session_state.alunos]))


sorteados = st.number_input("Digite o número de alunos a serem sorteados", min_value=1, max_value=len(st.session_state.alunos))
if st.button("Sortear"):
    if sorteados:
        sorteados = int(sorteados)
        if sorteados > len(st.session_state.alunos):
            st.warning(f"Não é possível sortear mais de {len(st.session_state.alunos)} alunos.")
        else:
            alunos_sorteados = random.sample(st.session_state.alunos, sorteados)
            st.success(f"Alunos sorteados:")
            for aluno in alunos_sorteados:
                st.write(f"- **[{aluno['id']:02d}] {aluno['nome']}**")
    else:
        st.warning("Informe o número de alunos a serem sorteados.")
if st.button("Limpar Sorteio"):
    st.empty()
if st.button("Randomizar Lista"):
    random.shuffle(st.session_state.alunos)
    st.rerun()
if st.button("Salvar Lista"):
    with open("alunos.json", "w") as f:
        json.dump(st.session_state.alunos, f)
    st.success("Lista de alunos salva em 'alunos.json'.")