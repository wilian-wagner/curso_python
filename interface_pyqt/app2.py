from PyQt5.QtWidgets import *
app = QApplication([])
button = QPushButton('Botão Clique')

def on_button_clicked():
    alert = QMessageBox()
    alert.setText('Mensagem Gerada com Sucesso!') 
    alert.exec_()

button.clicked.connect(on_button_clicked)
button.show() 
app.exec()
