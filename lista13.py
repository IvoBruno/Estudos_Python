import streamlit as st
import random

class tentativa():
    def __init__(self, numero):
        self.numero = numero
        self.chutes = []
        self.tentativas = 0

    def verificar_tentativa(self, chute):
        self.tentativas += 1
        self.chutes.append(chute)
        if chute < self.numero:
            return "Muito baixo! Tente novamente."
        elif chute > self.numero:
            return "Muito alto! Tente novamente."
        else:
            return f"Parabéns! Você acertou o número {self.numero} em {self.tentativas} tentativas."


st.set_page_config(page_title="Jogo da Advinhacao", page_icon=":dart:", layout="centered")
st.title("Jogo da Advinhacao :dart:",text_alignment = "center")
st.sidebar.title("Menu do jogo", text_alignment = "center")
st.sidebar.write("Bem-vindo ao jogo da adivinhação! Tente adivinhar o número secreto entre 1 e 100. Você receberá uma dica a cada tentativa. Boa sorte!")

if "atual" not in st.session_state:
    st.session_state.atual = tentativa(random.randint(1, 100))

if st.sidebar.button("Novo Jogo"):
    st.session_state.atual = tentativa(random.randint(1, 100))
    st.rerun()

atual = st.session_state.atual
valor_chute = st.number_input("Digite seu chute:", min_value=1, max_value=100, key="chute", width=200)
if st.button("Chutar"):
    resultado = atual.verificar_tentativa(valor_chute)
    if valor_chute == atual.numero:
        st.success(resultado)
    else:
        st.warning(resultado)
    st.write(f"Tentativas: {atual.tentativas}")
    st.write(f"Chutes anteriores: {atual.chutes}")