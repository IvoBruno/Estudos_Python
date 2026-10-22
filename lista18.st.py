import streamlit as st
import requests

api_url = "http://127.0.0.1:8000"

st.set_page_config(page_title="Quiz Tech", layout="centered")

st.title("QUIZ TECH")
st.caption("Aprenda e teste seus conhecimentos!")

if "acertos" not in st.session_state:
    st.session_state.acertos = 0
if "questao_atual" not in st.session_state:
    st.session_state.questao_atual = 0

try:
    resposta = requests.get(f"{api_url}/api")
    questoes = resposta.json() if resposta.status_code == 200 else []
except requests.exceptions.RequestException:
    questoes = []

if not questoes:
    st.warning("Não foi possível carregar as questões. Verifique se a API está rodando em http://127.0.0.1:8000")
    st.stop()

total = len(questoes)
idx = st.session_state.questao_atual

if idx < total:
    q = questoes[idx]
    with st.container(border=True):
        st.markdown(f"### Questão {idx + 1} de {total}")
        st.write(q["pergunta"])

        chaves = ["alternativa1", "alternativa2", "alternativa3", "alternativa4"]
        escolha = st.radio(
            "Selecione sua resposta:",
            options=chaves,
            format_func=lambda k: q[k],
            key=f"q_{idx}"
        )

        if st.button("Confirmar", use_container_width=True):
            if escolha == q["alternativa_correta"]:
                st.session_state.acertos += 1
            st.session_state.questao_atual += 1
            st.rerun()
else:
    with st.container(border=True):
        st.markdown("### 🎉 Quiz Finalizado!")
        st.write(f"Você acertou **{st.session_state.acertos}** de **{total}** questões.")
        if st.button("Reiniciar Quiz", use_container_width=True):
            st.session_state.questao_atual = 0
            st.session_state.acertos = 0
            st.rerun()
