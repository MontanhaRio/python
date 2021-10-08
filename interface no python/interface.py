from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')
layout = [
    [sg.Text('Usuario'),sg.Input(key='usuario',size=(20,1))],
    [sg.Text('Senha'),sg.Input(key='senha', password_char='*',size=(21,1))],
    [sg.Checkbox('Salvar 0 login?')],
    [sg.Button('Entrar')]
]
janela = sg.Window('Tela de Login', layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED:
        break
    if evento == 'Entrar':
        if valores['usuario'] == 'kenji' and valores['senha'] == '123456':
            print('Bem-vindo a Dev Aprender!')