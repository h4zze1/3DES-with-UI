import interface
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Ui(QWidget, interface.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Ui, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Ui()
    main.show()
    sys.exit(app.exec_())
