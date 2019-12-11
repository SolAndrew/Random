import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import random


class YS(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.drawCircle = False
        self.pushButton.clicked.connect(self.let_draw)
        self.CL = []

    def let_draw(self):
        self.drawCircle = True
        self.update()

    def DRAW(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        x, y = 500, 400
        cordx = random.randint(10, x - 10)
        cordy = random.randint(10, y - 10)
        r = random.randint(10, 90)
        self.CL.append([cordx, cordy, r, r])
        for i in self.CL:
            qp.drawEllipse(*i)

    def paintEvent(self, event):
        if self.drawCircle is True:
            qp = QPainter()
            qp.begin(self)
            self.DRAW(qp)
            qp.end()
            self.drawCircle = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YS()
    ex.show()
    sys.exit(app.exec_())