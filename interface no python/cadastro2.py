import PySimpleGUI as sg 
#criando layout
layout = [[sg.Combo(['choice 1', 'choice 2'])]]


#criando janela
janela = sg.Window("Dados do Usuario").layout(layout)


#abrindo janela janela
cadastro2 = janela()
