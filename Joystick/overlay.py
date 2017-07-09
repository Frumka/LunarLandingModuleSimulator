from PyQt4 import QtCore, QtGui, uic
from form import Ui_Form
import threading
import time
import sys

class OSD:
    def __init__(self, size = (640, 480), pos1 = (0, 0), pos2 = (0, 0)):
        app = QtGui.QApplication(sys.argv)
        window = QtGui.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(window)

        app2 = QtGui.QApplication(sys.argv)
        window2 = QtGui.QWidget()
        self.ui2 = Ui_Form()
        self.ui2.setupUi(window2)

        self.telem = None
        self.r = True

        self.mainThr = threading.Thread(target=self.update)
        self.mainThr.start()

        self.ui.move(*pos1)
        self.ui2.move(*pos2)
        self.ui.resize(size)
        self.ui2.resize(size)

        window.show()
        window2.show()
        sys.exit(app.exec_())

    def newTelemetry(self, telem):
        self.telem = telem

    def update(self):
        while self.r:
            if self.telem == None:
                continue

            self.ui.q1.setText(str(time.time()))
            self.ui.n1.display(111)
            time.sleep(1)