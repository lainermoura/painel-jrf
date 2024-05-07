import streamlit as st
import datetime as datetime
from components.header.header import show_header
from streamlit_modal import Modal
from streamlit_option_menu import option_menu
from page_link import page_link
from page_pautas_atas import page_pautas_atas

#Função para gerar o nome do arquivo


show_header()

# page = st.sidebar.selectbox('Menu', ('Publicações', 'Links'))
with st.sidebar:
    page = option_menu(
        menu_title=None,  
        options=["Publicações", "Links"],
        icons=["house", "link-45deg"],
    )

#Tipo, Sessão e Turma
if page == 'Publicações':
    page_pautas_atas()

elif page == 'Links':
    page_link()
    