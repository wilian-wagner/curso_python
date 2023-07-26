import PySimpleGUI as sg
# Definindo Conteúdo da Janela
layout = [[sg.Text("Qual Seu Nome ?")],
[sg.Input(key='-INPUT-')], 
[sg.Text(size=(40,1), key='-OUTPUT-')],
[sg.Button('Ok'), sg.Button('Sair')]]

# Criando a Janela
window = sg.Window('Hello World', layout)

while True:
    event, values = window.read()
# Validação usuario sair ou a janela foi fechada
    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break
# Criando a saída da Mensagem na Interface
    window['-OUTPUT-'].update('Olá ' + values['-INPUT-'] + " Gravando Saida na Interface")

window.close()