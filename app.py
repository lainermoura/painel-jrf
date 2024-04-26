import streamlit as st
import datetime as datetime

def generate_filename(tipo, sessao, turma, data, hora, distribuicao, num_ata_distrib):
    # Formatar a data e a hora no formato desejado
    data_str = data.strftime('%Y%m%d')
    hora_str = hora.strftime('%H%M')
    ano_str = data.strftime('%Y')

    # Remover o "ª" da turma e garantir que seja representada com dois dígitos
    if turma is not None:
        turma = f"{int(turma.replace('ª', '')):02d}"

    # Gerar o nome do arquivo
    #Tipo (Ata || Pauta) + Turma (00) + Sessão (000) + Ano (0000) + Data (YYYYMMDD) + Hora (HHMM) + Extensão
    #Exemplo: ATA-JRF00-000-0000-202401010800.pdf

    #ata de distribuição || Retificação da ata de distribuição
    #1-A-ATA-DISTRIBUICAO-JRF_202401010800.pdf
    #RETIFICACAO-1A-ATA-DISTRIBUICAO-JRF_AAAAMMDDHHMM.pdf

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

#Header|Subheader
st.header(':blue[Secretaria Municipal de Fazenda - Niterói]', divider='orange')

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
        num_ata_distrib = st.number_input('Digite o número da ata de distribuição:', 0, 1000)
        turma = None
        sessao = None
    else:
        #Turmas de 1 à 10
        turma = st.radio("Selecione a turma:", ['Selecione a opção'] + [f'{i}ª' for i in range(1, 11)])
        sessao = st.number_input('Digite a sessão:', 0, 1000)
        distribuicao = None
        num_ata_distrib = None

    # Verificar se o valor da sessão ou num_ata_distrib é 0
    if (sessao == 0 and tipo != 'Ata de Distribuição'):
        st.error('Digite o número da sessão.')
    elif (num_ata_distrib == 0 and tipo == 'Ata de Distribuição'):
        st.error('Digite o número da ata de distribuição.')
    elif (tipo != 'Ata de Distribuição' and turma == 'Selecione a opção') or (tipo == 'Ata de Distribuição' and distribuicao is None):
        st.error('Por favor, selecione todas as opções antes de prosseguir.')
    else:
        # Data
        date = datetime.date.today()
        data = st.date_input('Data da Reunião:', value=date, format='DD/MM/YYYY')

        # Verificar se a data é a data atual do sistema
        if data == date:
            st.warning(f'(Se a data de reunião não for HOJE, altere para a data desejada.)')

        # Hora
        hora = st.time_input('Hora da Reunião:', value=datetime.time(8, 0), step=1800)

        # Arquivo tipo pdf
        uploaded_file = st.file_uploader('Selecione o arquivo:', type=['pdf'])

        # Verificar se o arquivo foi carregado
        if hora.hour == 8 and hora.minute == 0:
            st.error('Por favor, revise a hora fornecida.')
        elif uploaded_file is None:
            st.error('Por favor, carregue um arquivo.')

        # Gerar o nome do arquivo
        if uploaded_file is not None and (hora.hour != 8 or hora.minute != 0):

            # Mostrar as opções selecionadas
            st.write('Opções selecionadas:')
            st.write('Tipo:', tipo)
            if tipo != 'Ata de Distribuição':
                st.write('Turma:', turma)
                st.write('Sessão:', sessao)
            else:
                st.write('Opção:', distribuicao)
                st.write('Número da Ata de Distribuição:', num_ata_distrib)
            if data == date:
                st.markdown(f'Data da Reunião: {data.strftime("%d/%m/%Y")} (**HOJE**)')

            else:
                st.write('Data da Reunião:', data.strftime('%d/%m/%Y'))
            st.write('Hora da Reunião:', hora.strftime('%H:%M'))

            filename = generate_filename(tipo, sessao, turma, data, hora, distribuicao, num_ata_distrib)
            st.write('Nome do arquivo:', filename)

            # Cria colunas
            col1, col2 = st.columns([1,1])

            # Alinhamento do botão
            with col2:
                if st.button('Publicar', on_click=''):
                    st.success('Arquivo publicado com sucesso!')