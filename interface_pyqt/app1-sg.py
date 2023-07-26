import PySimpleGUI as sg

layout = [[sg.Text("Ola Estou Criando uma Mensagem")], [sg.Button("OK")]]

# Criando a Janela
window = sg.Window("TITULO", layout)

# Criando o loop do evento
while True:
    event, values = window.read()
# Finalize o programa se o usuário fechar a janela ou pressiona OK if event == "OK" or event == sg.WIN_CLOSED:
    break 
window.close()