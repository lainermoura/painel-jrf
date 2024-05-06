import streamlit as st

def show_header():
    ocultar_menu = """
    <style>
    [data-testid="stHeader"] {visibility: hidden;}
    </style>
    """
    #Corpo do Streamlit
    st.image('logo-SMF.png', width=350)
    st.markdown(f'{ocultar_menu}<hr style="margin:0;border-bottom:2.5px solid #ed6f13;"/>', unsafe_allow_html=True)

    #Cria colunas para alinhar subheader à direita
    col1, col2 = st.columns([1,1])

    with col2:
        st.subheader(':blue[Junta de Revisão Fiscal]')

