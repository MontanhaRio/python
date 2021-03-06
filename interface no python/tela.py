import PySimpleGUI as sg 

class TelaPython:
    def __init__(self):
        #Layout
        layout = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(15,0),key='nome')],
            [sg.Text('Idade',size=(5,0)),sg.Input(size=(15,0),key='idade')],
            [sg.Text('Quais provedores de e-mail sao aceitos?')],
            [sg.Checkbox('Gmail',key='gmail'),sg.Checkbox('Outlook',key='outlook'),sg.Checkbox('Yahoo',key='yahoo')],
            [sg.Text('Aceita cartao')],
            [sg.Radio('Sim','cartoes',key='aceitaCartao'),sg.Radio('Nao','cartoes',key='NaoAceitaCartao')],
            [sg.Slider(range=(0,255),default_value=0,orientation='h',size=(15,20),key='slidervelocidade')],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30,20))]
        ]
        # Janela
        self.janela = sg.Window("Dados do Usuario").layout(layout)
        # Extrair os dados da tela
        
    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook =self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['NaoAceitaCartao']
            velocidade_script = self.values['slidervelocidade']
            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Aceita gmail: {aceita_gmail}')
            print(f'Aceita outlook: {aceita_outlook}')
            print(f'Aceita yahoo: {aceita_yahoo}')
            print(f'Aceita Cartao: {aceita_cartao}')
            print(f'Nao aceita Cartao: {nao_aceita_cartao}')
            print(f'Velocidade Scripts: {velocidade_script}')
    
tela = TelaPython()
tela.Iniciar()
