import sys
import pygame
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon, QMovie

class Jonkler(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jonkler")
        self.setWindowIcon(QIcon('assets/jonkler.jpeg'))
        self.setFixedSize(500,500)
        self.label1 = QLabel(self)
        self.labelimage = QLabel(self)
        self.button = QPushButton("Click me", self)
        self.image = QPixmap("assets/jonkler.jpeg")
        self.gifs = QMovie("assets/jonkler1.gif")
        self.initUI()

    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        self.label1.setText("Welcome to My Program")
        self.label1.setAlignment(Qt.AlignCenter)
        self.labelimage.setPixmap(self.image)
        self.labelimage.setScaledContents(True)

        self.label1.setObjectName("label1")
        self.labelimage.setObjectName("labelimage")
        self.button.setObjectName("button")
        
        self.setStyleSheet("""
            #label1 {
                font-size: 24px;
                font-weight: bold;
                border: 2px solid white;
            }
            #button {
                font-size: 24px;
                font-weight: bold;
                border: 2px solid black;
                padding: 10px 20px;
            }
            #button:hover {
                background-color: #7a7777;
                color: white;
            }
            #labelimage {
                width: 300px;
                height: 300px;
                
            }
        """)
        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.labelimage)
        layout.addWidget(self.button)
        central_widget.setLayout(layout)

        self.button.clicked.connect(self.buttonpressed)

    def buttonpressed(self):
        self.labelimage.setMovie(self.gifs)
        self.gifs.start()
        self.gifs.setScaledSize(self.image.size())
        pygame.init()
        sound = "assets/sound/whysoserious.mp3"
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play()
        self.label1.setText("Why so serious?")

        


def main():
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    app = QApplication(sys.argv)
    window = Jonkler()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()