import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon

class Jonkler(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jonkler")
        self.setWindowIcon(QIcon('assets/image/jonkler.png'))
        self.setGeometry(600,250,700, 700)
        self.initUI()

    def initUI(self):
        self.label = QLabel(self)
        pass

def main():
    app = QApplication(sys.argv)
    window = Jonkler()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()