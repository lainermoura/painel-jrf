import streamlit as st
import datetime as datetime
import time
import database

#Função para gerar o nome do arquivo
def generate_filename(tipo, sessao, turma, data, hora, distribuicao, num_ata_distrib):
    # Formatar a data e a hora no formato desejado
    data_str = data.strftime('%Y%m%d')
    hora_str = hora.strftime('%H%M')
    ano_str = data.strftime('%Y')

    # Remover o "ª" da turma e garantir que seja representada com dois dígitos
    if turma is not None:
        turma = f"{int(turma.replace('ª', '')):02d}"

    # Gerar o nome do arquivo
    extensao = '.pdf'
    tipo = tipo.upper()

    if tipo == 'PAUTA':
        filename = f"{tipo}-JRF{turma}{sessao:03d}{ano_str}_{data_str}{hora_str}{extensao}"
    elif tipo == 'ATA':
        filename = f"{tipo}-JRF{turma}{sessao:03d}{ano_str}_{data_str}{hora_str}{extensao}"
    elif tipo == 'ATA DE DISTRIBUIÇÃO':
        if distribuicao == 'Ata de Distribuição':
            filename = f"{num_ata_distrib}A-ATA-DISTRIBUICAO-JRF_{data_str}{hora_str}{extensao}"
        elif distribuicao == 'Retificação':
            filename = f"RETIFICACAO-{num_ata_distrib}A-ATA-DISTRIBUICAO-JRF_{data_str}{hora_str}{extensao}"
    return filename

ocultar_menu = """
    <style>
    [data-testid="stHeader"] {visibility: hidden;}
    </style>
    """

# st.title('')
#Corpo do Streamlit
st.image('logo-SMF.png', width=350)
st.markdown(f'{ocultar_menu}<hr style="margin:0;border-bottom:2.5px solid #ed6f13;"/>', unsafe_allow_html=True)
#Header|Subheader
# st.header('', divider='orange')

#Cria colunas para alinhar subheader à direita
col1, col2 = st.columns([1,1])

with col2:
    st.subheader(':blue[Junta de Revisão Fiscal]')

#Título
# st.title('Pautas, Atas e Atas de Distribuição')

#Tipo, Sessão e Turma
tipo = st.selectbox('Selecione o tipo:', ('Selecione a opção',  'Ata', 'Ata de Distribuição', 'Pauta'), key='tipo')

if tipo != 'Selecione a opção':
    if tipo == 'Ata de Distribuição':
        distribuicao = st.radio('Selecione a opção:', ['Ata de Distribuição', 'Retificação'], key='tipo_distribuicao')
        num_ata_distrib = None
        turma = None
        sessao = None
    else:
        #Turmas de 1 à 10
        turma = st.radio("Selecione a turma:", [f'{i}ª' for i in range(1, 11)], index=None, horizontal=True, key='turma')
        sessao = None
        distribuicao = None
        num_ata_distrib = None

    # Verificar se o valor da sessão ou num_ata_distrib é 0
    if turma is None and tipo != 'Ata de Distribuição':
        st.error('Por favor, selecione uma turma.')
    elif (sessao == 0 and tipo != 'Ata de Distribuição'):
        st.error('Digite o número da sessão.')
    elif (num_ata_distrib == 0 and tipo == 'Ata de Distribuição'):
        st.error('Digite o número da ata de distribuição.')
    elif (tipo != 'Ata de Distribuição' and turma == 'Selecione a opção') or (tipo == 'Ata de Distribuição' and distribuicao is None):
        st.error('Por favor, selecione todas as opções antes de prosseguir.')
    else:
        col1, col2, col3 = st.columns([1, 1, 1])

        with col1:
            if tipo != 'Ata de Distribuição':
                sessao = st.number_input('Digite a sessão:', 0, 1000, key='sessao')
            elif tipo == 'Ata de Distribuição':
                num_ata_distrib = st.number_input('Ata de distribuição nº:', 0, 1000, key='num_ata_distrib')

        desabilitado = True if (tipo == 'Ata de Distribuição' and num_ata_distrib == 0) or (tipo != 'Ata de Distribuição' and sessao == 0) else False

        with col2:
            # Data
            date = datetime.date.today()
            data = st.date_input('Data da Reunião:', value=None, format='DD/MM/YYYY', disabled=desabilitado, key='data')

        with col3:
            # Hora
            hora = st.time_input('Hora da Reunião:', value=datetime.time(8, 30), step=1800, disabled=desabilitado, key='hora')

        # Arquivo tipo pdf
        uploaded_file = st.file_uploader('Selecione o arquivo:', type=['pdf'], key='arquivo')

        # Verificar se o arquivo foi carregado
        if sessao == 0 and tipo != 'Ata de Distribuição':
            st.error('Por favor, forneça a sessão da reunião.')
        elif num_ata_distrib == 0 and tipo == 'Ata de Distribuição':
            st.error('Por favor, forneça o número da ata de distribuição.')
        elif data == None:
            st.error('Por favor, digite a data da reunião.')
        elif (hora.hour < 9) or (hora.hour > 18):
            st.error('Por favor, revise a hora fornecida.')
        elif uploaded_file is None:
            st.error('Por favor, carregue um arquivo.')

        # Condicional para selecionar o arquivo
        if uploaded_file is not None and (num_ata_distrib != 0 and sessao != 0 ) and data is not None and (hora.hour > 8) and (hora.hour <= 18):

            # Mostrar as opções selecionadas

            container = st.container(border=True)
            file_name = generate_filename(tipo, sessao, turma, data, hora, distribuicao, num_ata_distrib)

            selecionados = [
            ('Tipo', tipo),
            ('Turma', turma) if tipo != 'Ata de Distribuição' else None,
            ('Sessão', sessao) if tipo != 'Ata de Distribuição' else None,
            ('Opção', distribuicao) if tipo == 'Ata de Distribuição' else None,
            ('Número da Ata de Distribuição', num_ata_distrib) if tipo == 'Ata de Distribuição' else None,
            ('Data e hora da reunião', '{} às {}'.format(data.strftime("%d/%m/%Y"), hora.strftime("%Hh%M"))),
            ('Nome do arquivo', file_name)
        ]

            text = 'Opções selecionadas:\n\n'
            for selecao in [opcao for opcao in selecionados if opcao is not None]:
                if None not in selecao:  # Checar se None está na tupla
                    text += '* {}: {}\n'.format(*selecao)

            container.markdown(text)


            # Cria colunas
            col1, col2, col3 = st.columns([2,1,2])

            # Alinhamento do botão

            # Cria colunas
            col1, col2, col3 = st.columns([2,1,2])
            col4, col5, col6 = st.columns([.1, 2, .1])

            with col2:
                conn = database.create_connection()
                if st.button('Publicar'):
                    # Verificar se o arquivo foi carregado
                    if uploaded_file is not None:
                        file_data = uploaded_file.read()
                        file_name = generate_filename(tipo, sessao, turma, data, hora, distribuicao, num_ata_distrib)
                        database.create_files_table(conn)
                        if 'file_data' in locals() and 'file_name' in locals():
                            with col5:
                                if database.save_file_to_db(conn, file_data, file_name):
                                    success_message = f'{tipo} da **{sessao}ª sessão**  postada na **{turma} turma**!' if tipo != 'Ata de Distribuição' else f'{tipo} postada!'
                                    st.success(success_message)
                                    time.sleep(2)
                                    st.toast(f'{file_name}', icon='✅')
                                    time.sleep(1)
                                    turma_escolhida = f"{int(turma.replace('ª', ''))}" if turma is not None else None
                                    tipo_link = f'pautas-atas-de-julgamentos/#{turma_escolhida}' if distribuicao != 'Ata de Distribuição' else 'distribuicao/'
                                    st.toast(f'Confira aqui o arquivo: https://www.fazenda.niteroi.rj.gov.br/jrf/{tipo_link}', icon='✅')
                                else:
                                    st.error('Confira as informações fornecidas. Este nome/arquivo já existe.')


