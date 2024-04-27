import streamlit as st
import datetime as datetime


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


#Corpo do Streamlit
st.image('logo-SMF.png', width=350)
#Header|Subheader
st.header('', divider='orange')

#Cria colunas para alinhar subheader à direita
col1, col2 = st.columns([1,1])

with col2:
    st.subheader(':blue[Junta de Revisão Fiscal]')

#Título
st.title('Pautas, Atas e Atas de Distribuição')

#Tipo, Sessão e Turma
tipo = st.selectbox('Selecione o tipo:', ('Selecione a opção',  'Ata', 'Ata de Distribuição', 'Pauta'))

if tipo != 'Selecione a opção':
    if tipo == 'Ata de Distribuição':
        distribuicao = st.radio('Selecione a opção:', ['Ata de Distribuição', 'Retificação'])
        num_ata_distrib = None
        turma = None
        sessao = None
    else:
        #Turmas de 1 à 10
        turma = st.radio("Selecione a turma:", [f'{i}ª' for i in range(1, 11)], index=None, horizontal=True)
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
                sessao = st.number_input('Digite a sessão:', 0, 1000)
            elif tipo == 'Ata de Distribuição':
                num_ata_distrib = st.number_input('Ata de distribuição nº:', 0, 1000)

        desabilitado = True if (tipo == 'Ata de Distribuição' and num_ata_distrib == 0) or (tipo != 'Ata de Distribuição' and sessao == 0) else False

        with col2:
            # Data
            date = datetime.date.today()
            data = st.date_input('Data da Reunião:', value=None, format='DD/MM/YYYY', disabled=desabilitado)

        with col3:
            # Hora
            hora = st.time_input('Hora da Reunião:', value=datetime.time(8, 30), step=1800, disabled=desabilitado)

        # Arquivo tipo pdf
        uploaded_file = st.file_uploader('Selecione o arquivo:', type=['pdf'])

        # Verificar se o arquivo foi carregado
        if data == None:
            st.error('Por favor, digite a data da reunião.')
        elif hora.hour == 8 and hora.minute == 30:
            st.error('Por favor, revise a hora fornecida.')
        elif uploaded_file is None:
            st.error('Por favor, carregue um arquivo.')

        # Condicional para selecionar o arquivo
        if uploaded_file is not None and num_ata_distrib != 0 and data is not None and (hora.hour != 8 or hora.minute != 30):

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
            col1, col2 = st.columns([1,1])

            # Alinhamento do botão
            with col2:
                if st.button('Publicar', on_click=''):
                    st.success('Arquivo publicado com sucesso!')