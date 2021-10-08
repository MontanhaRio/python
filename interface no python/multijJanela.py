
import PySimpleGUI as sg

def janela_login():
    sg.theme('reddit')
    layou = [
        [sg.Text('Nome')],
        [sg.Input()],
        [sg.Button('Continuar')]
    ]
    return sg.Window('Login', layout=layou, finalize=True)

def janela_pedido():
    sg.theme('reddit')
    layou = [
        [sg.Text('Fazer Pedido')],
        [sg.Checkbox('Pizza Pepperoni', key ='p1'), sg.Checkbox('Pizza Frango c/ Catupiry', key ='p2')],
        [sg.Button('Voltar'), sg.Button('Fazer Pedido')]

    ]
    return sg.Window('Montar Pedido', layout=layou, finalize=True)
janela, janela2 = janela_login(), None
while True:
    window,event,values = sg.read_all_windows()
    if window == janela and event == sg.WIN_CLOSED:
        break
    if window == janela and event == 'Continuar':
        janela2 = janela_pedido()
        janela.hide()
    if window == janela2 and event == 'Voltar':
       janela2.hide()
       janela.un_hide() 
    if window == janela2 and event == 'Fazer Pedido':
        if values['p1'] == True and values['p2'] == True :
            sg.popup('Foram solicidado uma Pizza Pepperoni e uma Pizza Catupiry c/ Frango')
        elif values['p1'] == True :
            sg.popup('Foi solicidado uma Pizza Pepperoni')
        elif values['p2'] == True :
            sg.popup('Foi solicidado uma Pizza Catupity c/ Frango')