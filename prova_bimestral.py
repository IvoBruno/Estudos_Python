import streamlit as st

st.set_page_config(page_title="IMC", page_icon=":memo:", layout="centered")
with st.container(border=True, gap="xxsmall", horizontal_alignment="center"):
    st.title("IMC Inteligente")
    st.caption("Sua saúde começa com informação")
with st.container(border=True, horizontal_alignment="center"):
    st.markdown("## Calcule seu IMC", text_alignment="center")
    st.markdown("Preencha os dados abaixo para calcular seu índice de massa corporal (IMC).")
    col1, col2 = st.columns(2)
    with col1:
        peso = st.number_input("Peso (kg):", min_value=1.0, max_value=500.0, step=0.5)
    with col2:
        altura = st.number_input("Altura (m):", min_value=0.5, max_value=3.0, step=0.01)
    if st.button("Calcular IMC", use_container_width=True):
        if altura > 0 and peso > 0:
            st.caption("Resultado do IMC", text_alignment="center")
            imc = peso / (altura ** 2)
            st.markdown(f"# {imc:.2f}", text_alignment="center")
            if imc < 18.5:
                st.warning(":warning: Você está abaixo do peso ideal.")
            elif 18.5 <= imc < 24.9:
                st.success(":white_check_mark: Você está com o peso ideal.")
            elif 25 <= imc < 29.9:
                st.warning(":warning: Você está acima do peso ideal.")
            else:
                st.error(":bangbang: Você está com obesidade.")
        else:
            st.error("A altura e o peso devem ser maiores que zero.")
    st.caption("O IMC é um indicador geral e não substitui uma avaliação profissional de saúde.")