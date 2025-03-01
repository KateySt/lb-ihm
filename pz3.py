from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        # Ініціалізація елементів управління
        self.initUI()

    def initUI(self):
        # Створення кнопки
        self.button = QPushButton('Натисни мене', self)
        self.button.clicked.connect(self.on_click)

        # Створення вертикального макету
        vbox = QVBoxLayout()
        vbox.addWidget(self.button)

        self.setLayout(vbox)

        # Налаштування основного вікна
        self.setWindowTitle('Мій простий інтерфейс')
        self.setGeometry(300, 300, 300, 200)

    def on_click(self):
        # Зміна кольору фону вікна
        self.setStyleSheet("background-color: lightblue;")

if __name__ == '__main__':
    app = QApplication([])
    window = MyApp()
    window.show()
    app.exec_()
