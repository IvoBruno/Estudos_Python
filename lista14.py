import streamlit as st

st.set_page_config("Portal Turismo", page_icon=":airplane:", layout="centered")
st.title("Portal Turismo, Conheca os melhores destinos!", text_alignment = "center")
st.image("assets/images/logo.png")
st.sidebar.title("Menu do Portal Turismo", text_alignment = "center")
st.sidebar.write(":round_pushpin: Destinos\n\n:camera: Galerias\n\n:file_folder: Materiais\n\n:link: Links\n\n:telephone_receiver: Contato\n\n:star: Avaliações")
st.text(" Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
st.text("Conheca a cidade de Parnaíba, a Princesa do Delta!")
st.image("assets/images/princesa_do_delta.png")
st.text("Todos os direitos reservados © 2026 - Portal Turismo")