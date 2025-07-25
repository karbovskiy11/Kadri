import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_MainWindow
from connection import Data


class GeneralWindow(QMainWindow):
    def __init__(self):
        super(GeneralWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect = Data()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GeneralWindow()
    window.show()

    sys.exit(app.exec())