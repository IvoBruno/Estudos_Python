import streamlit as st
import requests

def text_to_value(text):
    if text == "ACE":
        return 14
    elif text == "KING":
        return 13
    elif text == "QUEEN":
        return 12
    elif text == "JACK":
        return 11
    else:
        return int(text)
def traduz_naipe(naipe):
    if naipe == "HEARTS":
        return "Copas"
    elif naipe == "DIAMONDS":
        return "Ouros"
    elif naipe == "CLUBS":
        return "Paus"
    elif naipe == "SPADES":
        return "Espadas"
st.set_page_config("Jogo de Cartas", page_icon=":game_die:", layout="centered")
st.title(":game_die: Jogo de Cartas", text_alignment = "center")
deck = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1").json()
p1 = requests.get(f"https://deckofcardsapi.com/api/deck/{deck['deck_id']}/draw/?count=1").json()
p2 = requests.get(f"https://deckofcardsapi.com/api/deck/{deck['deck_id']}/draw/?count=1").json()
c1, c2 = st.columns([1, 1])
c1.write("**Jogador 1**")
c2.write("**Jogador 2**")
with c1:
    st.image(p1['cards'][0]['image'], width=200)
    st.text(f"{p1['cards'][0]['value']} de {traduz_naipe(p1['cards'][0]['suit'])}")
with c2:
    st.image(p2['cards'][0]['image'], width=200)
    st.text(f"{p2['cards'][0]['value']} de {traduz_naipe(p2['cards'][0]['suit'])}")
if text_to_value(p1['cards'][0]['value']) > text_to_value(p2['cards'][0]['value']):
    st.success("Jogador 1 venceu!")
elif text_to_value(p1['cards'][0]['value']) < text_to_value(p2['cards'][0]['value']):
    st.success("Jogador 2 venceu!")
else:
    st.warning("Empate!")
st.text("Todos os direitos reservados © 2026 - Jogo de Cartas")