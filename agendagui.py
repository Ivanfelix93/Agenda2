import PySimpleGUI as sg

# Defina o layout da interface gráfica
layout = [
    [sg.Text('Agenda')],
    [sg.Text("Nome",size=(10,0)), sg.Input(size=(15,0),key="nome")],
    [sg.Text('Telefone:', size=(10,0)), sg.InputText(size=(15,0),key='telefone')],
    [sg.Text('email:', size=(10,0)), sg.InputText(size=(15,0),key='email')],
    [sg.Text('cep:', size=(10,0)), sg.InputText(size=(15,0),key='cep')],
    [sg.Button('Salvar'), sg.Button('Cancelar')]
]


sg.theme('Dark Brown 1')

# Crie a janela da interface gráfica
window = sg.Window('Agenda').Layout(layout)

# Loop principal do programa
while True:
    event, values = window.Read()

    # Fechar a janela se o usuário pressionar o botão 'Cancelar' ou fechar a janela
    if event == sg.WINDOW_CLOSED or event == 'Cancelar':
        break

    # Salvar os dados se o usuário pressionar o botão 'Salvar'
    if event == 'Salvar':
        nome = values['nome']
        telefone = values['telefone']
        email = values['email']
        cep = values['cep']



        # Salvar os dados em um arquivo ou banco de dados, por exemplo
        print(f'Nome: {nome}, Telefone: {telefone}, email: {email}, cep`{cep}')

# Fechar a janela e sair do programa
window.Close()
