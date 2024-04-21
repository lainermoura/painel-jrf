import streamlit as st
import datetime as datetime

def generate_filename(tipo, sessao, turma, data, hora):
    # Formatar a data e a hora no formato desejado
    data_str = data.strftime('%Y%m%d')
    hora_str = hora.strftime('%H%M')
    ano_str = data.strftime('%Y')

    # Remover o "ª" da turma e garantir que seja representada com dois dígitos
    turma = f"{int(turma.replace('ª', '')):02d}"

    # Gerar o nome do arquivo
    if tipo.lower() == 'pauta':
        filename = f"{tipo.upper()}-JRF{turma}{sessao:02d}{ano_str}_{data_str}{hora_str}"
    elif tipo.lower() == 'ata':
        filename = f"{tipo.upper()}-JRF{turma}{sessao:03d}{ano_str}_{data_str}{hora_str}"
    return filename


#Título
st.title('Painel de Controle - JRF')

#Tipo, Sessão e Turma
tipo = st.selectbox('Selecione o tipo:', ['Selecione a opção', 'Pauta', 'Ata'])
turma = st.radio('Selecione a turma:', ['Selecione a opção'] + [f'{i}ª' for i in range(1, 11)])
sessao = st.number_input('Digite a sessão:', 0, 1000)

# Verificar se o valor da sessão é 0
if sessao == 0:
    st.error('Digite o número da sessão.')
elif tipo == 'Selecione a opção' or turma == 'Selecione a opção':
    st.error('Por favor, selecione todas as opções antes de prosseguir.')
else:
    # Data
    data = st.date_input('Data da Reunião:', value=datetime.datetime(1900, 1, 1))
    #Hora
    hora = st.time_input('Hora da Reunião:', value=datetime.time(0, 0))

    #Arquivo
    uploaded_file = st.file_uploader('Selecione o arquivo:')

    # Gerar o nome do arquivo
    if uploaded_file is not None and data.year != 1900 and (hora.hour != 0 or hora.minute != 0):
        # Display the selected options
        st.write('Opções selecionadas:')
        st.write('Tipo:', tipo)
        st.write('Turma:', turma)
        st.write('Sessão:', sessao)
        st.write('Data da Reunião:', data)
        st.write('Hora da Reunião:', hora)

        filename = generate_filename(tipo, sessao, turma, data, hora)
        st.write('Nome do arquivo:', filename)

        # Create columns
        col1, col2 = st.columns([1,1])

        # Place the button in the right column
        with col2:
            if st.button('Publicar'):
                st.success('Arquivo publicado com sucesso!')
    else:
        st.error('Por favor, selecione todas as opções e carregue um arquivo antes de clicar em Publicar.')
