import streamlit as st
from components.header.header import show_header
from st_keyup import st_keyup
from streamlit_modal import Modal
from streamlit_option_menu import option_menu
import re
import database
from streamlit.components.v1 import html
from turmas import turmas


def page_link():
    turma_numero = st.radio("Selecione a turma:", [f'{i+1}ª' for i in range(0,10)], index=None, horizontal=True)
    if turma_numero is not None:
        text_placeholder = f'Insira aqui o link da turma.'
        link_reuniao = st_keyup('Link:', placeholder=text_placeholder)
        # link_reuniao = st.text_input('Link:', placeholder=text_placeholder, key='link')

        with open('script.js', 'r') as file:
            evento_colar = f"<script>{file.read()}</script>"
            html(evento_colar)
            # html(f'<script>console.log("{evento_colar}");</script>')

        padrao_https = r'\b((?:^(https?:\/\/))([a-zo0-9]+)|(^[a-zo0-9]+))\.([a-zo0-9]+)\.com\/.*\b'

        modal = Modal(
    f"Confirma a atualização do link da {turma_numero} turma?",  
    key="meu-modal",  
    padding=20,  
    max_width=800  
    )
        if re.match(padrao_https, link_reuniao):
            id_turma = turma_numero.replace('ª', '')
            turma_selecionada = turmas[int(id_turma)]
            def escreva_turma():
                st.write(f"""

                    Presidente: {turma_selecionada.presidente}

                    Julgadores: {', '.join(turma_selecionada.julgadores)}
                    
                    Secretário: {turma_selecionada.secretario}
                    """)
            escreva_turma()
            open_modal = st.button("Prosseguir")

            if open_modal:
                modal.open()
            if modal.is_open():
                with modal.container():
                    escreva_turma()
                    col1,col2,col3=st.columns([1,1,1])
                    with col3:
                        if st.button(f'Atualizar link da {turma_numero} turma.'):
                            conn = database.create_connection()
                            database.create_turma_table(conn)
                            if database.save_link_to_db(conn, link_reuniao, id_turma):
                                st.success('Link atualizado!')
                            else:
                                st.error('Confira as informações fornecidas. Este link já existe.')    
