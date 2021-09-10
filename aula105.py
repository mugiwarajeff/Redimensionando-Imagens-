import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap, QIcon
from design import *

class Aplicativo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnabrir.clicked.connect(self.abrir)
        self.btnredimensionar.clicked.connect(self.redimen)
        self.btnsalvar.clicked.connect(self.salvar)
        self.setWindowTitle("Redimensionando Imagens By: Jeff")
        self.btnsalvar.setDisabled(True)
        self.setWindowIcon(QIcon("redimensionar-expandir.png"))

    def abrir(self):
        imagem, _ = QFileDialog.getOpenFileName(self.centralwidget, "untitle", r"C:\Users\jeffe\Downloads")
        self.inputabrir.setText(imagem)
        self.imagem_original = QPixmap(imagem)
        self.label.setPixmap(self.imagem_original)
        self.inpurlargura.setText(str(self.imagem_original.width()))
        self.inputaltura.setText(str(self.imagem_original.height()))


    def redimen(self):
        largura = int(self.inpurlargura.text())
        self.nova_imagem = self.imagem_original.scaledToWidth(largura)
        self.label.setPixmap(self.nova_imagem)
        self.inputaltura.setText(str(self.nova_imagem.height()))
        self.inpurlargura.setText(str(self.nova_imagem.width()))
        self.btnsalvar.setDisabled(False)

    def salvar(self):
        imagem, _ = QFileDialog.getSaveFileName(self.centralwidget, "Janela para salvar", r"C:\Users\jeffe\Downloads")
        self.nova_imagem.save(imagem, "png")

if __name__ == "__main__":
    sys = QApplication(sys.argv)
    app = Aplicativo()
    app.show()
    sys.exec_()


